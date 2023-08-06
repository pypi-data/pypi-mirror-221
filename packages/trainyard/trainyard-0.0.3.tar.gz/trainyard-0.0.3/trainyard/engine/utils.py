import random
import string
from typing import Optional

from trainyard.engine.cluster import Cluster, RemoteObject  # noqa
from trainyard.engine.local import LocalCluster
from trainyard.engine.runhouse import RunhouseCluster

CLUSTER_MAP = {"local": LocalCluster, "runhouse": RunhouseCluster}


class BACKEND_MANAGER:
    BACKENDS = ["runhouse", "local"]
    DEFAULT_BACKEND = "runhouse"


def is_available(backend: str) -> bool:
    if backend == "runhouse":
        try:
            import runhouse  # noqa

            return True
        except Exception:
            return False
    return True


def set_default_backend(backend: str) -> None:
    """
    Sets default backend

    Args:
        backend (str): sets default backend
    """
    if backend not in BACKEND_MANAGER:
        raise ValueError(
            f"backend {backend} not supported! Available backends: {BACKEND_MANAGER.BACKENDS}"
        )
    BACKEND_MANAGER.DEFAULT_BACKEND = backend


def cluster(
    backend: str = "runhouse",
    name: Optional[str] = None,
    instance_type: Optional[str] = None,
    **kwargs,
):
    if name is None:
        name = "".join(random.choice(string.lowercase) for x in range(10))
        name = f"{backend}-cluster-{name}"
    cluster_class = CLUSTER_MAP.get(backend, RunhouseCluster)
    return cluster_class(name, instance_type, **kwargs)


class ClusterSpec:
    def __init__(
        self, name: Optional[str] = None, instance_type: Optional[str] = None, **kwargs
    ):
        if name is None:
            name = "".join(
                random.choice(string.ascii_uppercase + string.digits) for _ in range(12)
            )
            name = f"cluster-{name}"
        self.name = name
        self.instance_type = instance_type
        self.kwargs = kwargs

    def create_cluster(self) -> Cluster:
        if is_available(BACKEND_MANAGER.DEFAULT_BACKEND):
            return cluster(
                backend=BACKEND_MANAGER.DEFAULT_BACKEND,
                name=self.name,
                instance_type=self.instance_type,
                **self.kwargs,
            )

        for backend in BACKEND_MANAGER.BACKENDS:
            # skip default backend
            if backend != BACKEND_MANAGER.DEFAULT_BACKEND and is_available(backend):
                return cluster(
                    backend=backend,
                    name=self.name,
                    instance_type=self.instance_type,
                    **self.kwargs,
                )
