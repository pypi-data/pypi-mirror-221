from typing import Any

import runhouse as rh

from trainyard.engine.engine import ClusterSpec, Engine


class RunhouseEngine(Engine):
    def make_cluster(self, cluster_spec: ClusterSpec) -> Any:
        if cluster_spec.instance_type is None:
            cluster = rh.cluster(
                name=cluster_spec.name,
                ips=cluster_spec.ips,
                ssh_creds=cluster_spec.ssh_creds,
                *cluster_spec.args,
                **cluster_spec.kwargs,
            )
        else:
            cluster = rh.cluster(
                name=cluster_spec.name,
                instance_type=cluster_spec.instance_type,
                *cluster_spec.args,
                **cluster_spec.kwargs,
            )
        if cluster_spec.start:
            cluster.up_if_not()
        return cluster

    def put(self, key: str, obj: Any, cluster_spec: ClusterSpec) -> str:
        cluster = self.make_cluster(cluster_spec=cluster_spec)
        return cluster.put(key, obj)

    def get(self, key: str, cluster_spec: ClusterSpec) -> Any:
        cluster = self.make_cluster(cluster_spec=cluster_spec)
        return cluster.get(key)

    # def run(
    #     self,
    #     fn: Callable[[Any], Any],
    #     *args,
    #     cluster_spec: Optional[ClusterSpec] = None,
    #     config: Dict[str, Any] = {},
    #     **kwargs,
    # ):
    #     cluster = self.make_cluster(cluster_spec)
    #     function = rh.function()
