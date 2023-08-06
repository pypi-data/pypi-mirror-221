import abc
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class ClusterSpec:
    name: str
    backend: str = "local"
    env_requirements: Optional[List[Any]] = field(default_factory=lambda: None)
    instance_type: Optional[str] = None
    ips: Optional[List[str]] = None
    ssh_creds: Optional[dict] = None
    start: bool = True
    args: List[Any] = field(default_factory=lambda: [])
    kwargs: Dict[str, Any] = field(default_factory=lambda: {})


def cluster(
    name: str,
    *args,
    backend: str = "local",
    env_requirements: Optional[List[Any]] = None,
    instance_type: Optional[str] = None,
    ips: Optional[List[str]] = None,
    ssh_creds: Optional[dict] = None,
    **kwargs,
) -> ClusterSpec:
    return ClusterSpec(
        name, backend, env_requirements, instance_type, ips, ssh_creds, args, kwargs
    )


class Engine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def put(self, key: str, obj: Any, cluster_spec: ClusterSpec) -> str:
        """
        Pin object to memory

        Args:
            key (str): key to the object to save
            obj (Any): object
            cluster_spec (ClusterSpec): cluster specification to determine the creation of the cluster

        Returns:
            str: key of the object
        """

    @abc.abstractmethod
    def get(self, key: str, cluster_spec: ClusterSpec) -> Any:
        """
        Gets the object with a given key from a cluster with cluster name

        Args:
            key (str): key of object to retrieve
            cluster_spec (ClusterSpec): cluster specification to determine the creation of the cluster
        """

    @abc.abstractmethod
    def run(
        self,
        fn: Callable[[Any], Any],
        *args,
        cluster_spec: Optional[ClusterSpec] = None,
        **kwargs,
    ):
        """
        Run remote function with cluster spec

        Args:
            fn (Callable[[Any], Any]): function to run on cluster
            cluster_spec (Optional[ClusterSpec], optional): Cluster specification. Defaults to None.
        """
