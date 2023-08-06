from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import runhouse as rh

from trainyard.engine.cluster import Cluster, RemoteObject


def create_runhouse_cluster(name: str, instance_type: str, **kwargs):
    if rh.exists(name, "cluster"):
        return rh.cluster(name)
    cluster = rh.cluster(name=name, instance_type=instance_type, **kwargs)
    cluster.save()
    return cluster


# runhouse needs function to be exposed
def _run_remote(*args, runnable_fn=None, **kwargs):
    _args = []
    for arg in args:
        _arg = arg
        if isinstance(_arg, RemoteObject):
            _arg = _arg.get_result()
        _args.append(_arg)

    _kwargs = {}
    for kw in kwargs:
        _kwargs[kw] = kwargs[kw]
        if isinstance(_kwargs[kw], RemoteObject):
            _kwarg = _kwargs[kw].get_result()
            kwargs[kw] = _kwarg
    return runnable_fn(*_args, **_kwargs)


class RunhouseCluster(Cluster):
    def __init__(self, name: str, instance_type: str, **kwargs):
        """
        Creates a runhouse cluster with args. For a full list: https://runhouse-docs.readthedocs-hosted.com/en/latest/_modules/runhouse/rns/hardware/cluster_factory.html#cluster
        """
        super().__init__(name, instance_type)
        self.cluster = create_runhouse_cluster(
            name=name, instance_type=instance_type, **kwargs
        )

    def install_packages(self, packages: List[str]) -> None:
        rh_packages = []
        for package in packages:
            rh_packages.append(package)
        self.cluster.install_packages(rh_packages)

    def system(self, commands: List[str], *args, **kwargs):
        """
        Run bash commands on the cluster.
        For more details: https://runhouse-docs.readthedocs-hosted.com/en/latest/api/python/cluster.html

        Args:
            commands (List[str]): commands to run
        """
        self.cluster.run(commands, *args, **kwargs)

    def run(
        self,
        fn: Callable[[Any], Any],
        *args,
        name: Optional[str] = None,
        packages: Optional[List[str]] = None,
        env_requirements: Optional[Union[List[str], str]] = None,
        resources: Optional[Dict[str, Any]] = None,
        cluster_run_config: Dict[str, Any] = {},
        **kwargs,
    ) -> Tuple[str, Any]:
        """
        Wraps the function in a runhouse.function and automatically attaches it to the runhouse cluster.
        For a full list of Function parameters: https://runhouse-docs.readthedocs-hosted.com/en/latest/api/python/function.html#function-class

        Args:
            fn (Callable[[Any], Any]): Callable function
            name (str): name of the function
            packages (Optional[List[str]]): Packages to install. Defaults to None
            env_requirements (Optional[Union[List[str], str]], optional): Environment requirements of the function. Defaults to None.
            resources (Optional[Dict[str, Any]], optional): resources of the function. Optional number (int) of resources needed to run the Function on the Cluster. Keys must be num_cpus and num_gpus. Defaults to None.
            cluster_run_config (Dict[str, Any], optional): Additional parameters, see https://runhouse-docs.readthedocs-hosted.com/en/latest/api/python/function.html#function-class. Defaults to {}.

        Returns:
            str: output name
            Any: function output
        """

        self.cluster.up_if_not()
        if packages is not None:
            self.install_packages(packages)

        remote_fn = rh.function(
            fn=_run_remote,
            name=name,
            system=self.cluster,
            env=env_requirements,
            resources=resources,
            **cluster_run_config,
        )
        ref = remote_fn.run(*args, runnable_fn=fn, **kwargs)
        return RemoteObject(
            name=ref.name,
            remote_output_ref=ref,
            cluster=self,
            cluster_name=self.name,
        )

    def put(self, key: str, obj: Any, *args, **kwargs) -> str:
        """
        https://runhouse-docs.readthedocs-hosted.com/en/latest/_modules/runhouse/rns/hardware/cluster.html#Cluster.put

        puts object in object store in cluster

        Args:
            key (str): Put the given object on the cluster's object store at the given key.
            obj (Any): _description_

        Returns:
            str: _description_
        """
        self.cluster.put(key, obj, *args, **kwargs)
        return key

    def get(self, key: str, *args, **kwargs) -> Any:
        """
        https://runhouse-docs.readthedocs-hosted.com/en/latest/_modules/runhouse/rns/hardware/cluster.html#Cluster.get

        Get the result for a given key from the cluster's object store.

        Args:
            key (str): key to retrieve from runhouse object store

        Returns:
            Any: object in the object store
        """
        return self.cluster.get(key, *args, **kwargs)

    def start(self) -> RunhouseCluster:
        self.cluster.up_if_not()
        return self

    def teardown(self) -> None:
        # replace this with `teardown_and_delete` when it works
        self.cluster.teardown()
        self.cluster.unname()

    def save_blob(self, name: str, data: Any, *args, **kwargs) -> str:
        """
        Saves a blob of data into a datastore. For full configuration: https://runhouse-docs.readthedocs-hosted.com/en/latest/api/python/blob.html#blob-factory-method

        Args:
            name (str): name of the blob to save
            data (Any): data to save

        Returns:
            str: name of the blob
        """
        rh.blob(name=name, data=data, *args, **kwargs)
        return name

    def retrieve_blob(self, name: str, *args, **kwargs) -> rh.Blob:
        """
        Retrieves blob of data from datastore.1

        Args:
            name (str): name of blob to retrieve

        Returns:
            rh.Blob: blob object from datastore
        """
        return rh.blob(name=name, *args, **kwargs)
