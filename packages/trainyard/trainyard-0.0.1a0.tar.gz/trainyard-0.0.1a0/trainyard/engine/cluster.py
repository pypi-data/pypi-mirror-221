from __future__ import annotations

import abc
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Union


@dataclass
class RemoteObject:
    name: str
    remote_output_ref: Optional[Any] = None  # reference to remote output
    cluster: Optional[Cluster] = None
    cluster_name: Optional[str] = None

    def get_result(self) -> Any:
        if self.cluster is None and self.remote_output_ref is None:
            raise ValueError("Remote output or cluster must be specified!")
        if self.cluster is None:
            return self.remote_output_ref
        return self.cluster.get(self.name, stream_logs=True)


class Cluster(metaclass=abc.ABCMeta):
    def __init__(self, name: str, instance_type: str):
        """
        Args:
            name (str): Name of the cluster
            instance_type (str, optional): Instance type. This could be a resource (GPU:2) or a type (V100). Defaults to None.
        """
        self.name = name
        self.instance_type = instance_type

    def install_packages(self, packages: List[str]) -> None:
        """
        Install packages

        Args:
            packages (List[str]): package list, format: <install_method>:<package_name>. eg: pip:trainyard

        """
        pass

    @abc.abstractmethod
    def run(
        self,
        fn: Callable[[Any], Any],
        name: str,
        packages: Optional[List[str]] = None,
        env_requirements: Optional[Union[List[str], str]] = None,
        resources: Optional[Dict[str, Any]] = None,
        config: Dict[str, Any] = {},
        *args,
        **kwargs,
    ) -> RemoteObject:
        """
        Run remote function and return a reference if needed!

        Args:
            fn (Callable[[Any], Any]): _description_
            name (str): _description_
            env_requirements (Optional[Union[List[str], str]], optional): _description_. Defaults to None.
            resources (Optional[Dict[str, Any]], optional): _description_. Defaults to None.
            config (Dict[str, Any], optional): _description_. Defaults to {}.

        Returns:
            RemoteObject: remote object
        """

    @abc.abstractmethod
    def put(self, key: str, obj: Any, *args, **kwargs) -> str:
        """
        Put the given object on the cluster's object store at the given key.

        Args:
            key (str): name of object to save
            obj (Any): object to save

        Returns:
            str: name of object
        """

    @abc.abstractmethod
    def get(self, key: str, *args, **kwargs) -> Any:
        """
        Get the result for a given key from the cluster's object store.

        Args:
            key (str): key of the object to get

        Returns:
            Any: object retrieved from object store
        """

    def start(self) -> str:
        """
        Starts the clster

        Returns:
            str: address of cluster
        """
        return "local"

    def teardown(self) -> None:
        """
        Teardown and delete the cluster
        """
        pass

    def save_blob(self, name: str, data: Any, *args, **kwargs) -> str:
        """
        Saves blob to the cluster with associated name. By default just calls put

        Args:
            name (str): Name of object to save
            data (Any): content to save

        Returns:
            str: name of content
        """
        return self.put(key=name, obj=data, *args, **kwargs)

    def retrieve_blob(self, name: str, *args, **kwargs) -> Any:
        """
        Retrieves a blob from the cluster with associated name. By default just calls get

        Args:
            name (str): name of object to retrieve

        Returns:
            Any: Retrieved type can be anything. This may be a ref to the object itself
        """
        return self.get(key=name, *args, **kwargs)
