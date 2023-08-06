from __future__ import annotations

import abc
from typing import Any, Callable, Dict, List, Optional, Type, Union

from trainyard.engine import Cluster, ClusterSpec, RemoteObject


class TaskWrapper:
    def wrap(self, f: Callable[[Any], Any], task: Task) -> Callable[[Any], Any]:
        return f


class GLOBAL_TASK_WRAPPER:
    task_wrapper: Optional[TaskWrapper] = None

    @staticmethod
    def set_task_wrapper(task_wrapper: TaskWrapper):
        GLOBAL_TASK_WRAPPER.task_wrapper = task_wrapper

    @staticmethod
    def get_task_wrapper():
        return GLOBAL_TASK_WRAPPER.task_wrapper


class TaskOptions:
    """
    Args:
        name (str): name of the task
        packages (Optional[List[str]]): Packages to install for the task. Defaults to None
        env_requirements (Optional[Union[List[str], str]], optional): List of requirements to install on the remote cluster, or path to the requirements.txt file.  Defaults to None.
        resources (Optional[Dict[str, Any]], optional): Optional number (int) of resources needed to run the Function on the Cluster. Keys must be num_cpus and num_gpus.. Defaults to None.
        cluster (ClusterSpec, optional): cluster specification to run on. Defaults to ClusterSpec().
        cluster_run_config (Dict[str, Any], optional): additional config for building the remote function. Defaults to {}.
        description (str): Description for the task.
    """

    def __init__(
        self,
        packages: Optional[List[str]] = None,
        env_requirements: Optional[Union[List[str], str]] = None,
        resources: Optional[Dict[str, Any]] = None,
        cluster: ClusterSpec = ClusterSpec(),
        cluster_run_config: Dict[str, Any] = {},
        description: str = "",
    ):
        self.packages = packages
        self.env_requirements = env_requirements
        self.resources = resources
        self.cluster = cluster
        self.cluster_run_config = cluster_run_config
        self.description = description

    def merge(self, **kwargs) -> TaskOptions:
        return self.__class__(**{**self.to_dict(), **kwargs})

    def to_dict(self) -> Dict[str, Any]:
        return {
            "packages": self.packages,
            "env_requirements": self.env_requirements,
            "resources": self.resources,
            "cluster": self.cluster,
            "cluster_run_config": self.cluster_run_config,
            "description": self.description,
        }


def task_options(options: Optional[TaskOptions] = None, **kwargs) -> Type[Task]:
    def dec(task):
        if options is not None:
            task.options = task.options.merge({**options.to_dict(), **kwargs})
            return task
        task.options = task.options.merge(**kwargs)
        return task

    return dec


def run_fn(_task, *args, **kwargs):
    return _task(*args, **kwargs)


class Task(metaclass=abc.ABCMeta):
    options: TaskOptions = TaskOptions()

    def __init__(
        self,
        name: str,
    ):
        """
        Base Task object. This is the main runnable function for workflows to run

        Args:
            name (str): name of the task

        Options:
            name (str): name of the task
            packages (Optional[List[str]]): Packages to install for the task. Defaults to None
            env_requirements (Optional[Union[List[str], str]], optional): List of requirements to install on the remote cluster, or path to the requirements.txt file.  Defaults to None.
            resources (Optional[Dict[str, Any]], optional): Optional number (int) of resources needed to run the Function on the Cluster. Keys must be num_cpus and num_gpus.. Defaults to None.
            cluster (ClusterSpec, optional): cluster specification to run on. Defaults to ClusterSpec().
            cluster_run_config (Dict[str, Any], optional): additional config for building the remote function. Defaults to {}.
            description (str): Description for the task.
        """
        self.name = name
        self.options = self.__class__.options

    @property
    def cluster(self) -> Union[ClusterSpec, Cluster]:
        return self.options.cluster

    @cluster.setter
    def cluster(self, cluster: Union[ClusterSpec, Cluster]) -> None:
        self.options.cluster = cluster

    def set_options(self, options: TaskOptions = TaskOptions(), **kwargs) -> None:
        self.options = options.merge(**kwargs)

    def to(self, cluster: Cluster) -> Task:
        self.cluster = cluster
        return self

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        """
        Main function for task.
        """

    def remote(
        self, *args, cluster: Optional[Cluster] = None, **kwargs
    ) -> RemoteObject:
        if cluster is None:
            if isinstance(self.cluster, ClusterSpec):
                self.cluster = self.cluster.create_cluster()
            cluster = self.cluster

        remote_output = cluster.run(
            run_fn,
            name=self.name,
            packages=self.options.packages,
            env_requirements=self.options.env_requirements,
            resources=self.options.resources,
            cluster_run_config=self.options.cluster_run_config,
            _task=self,
            *args,
            **kwargs,
        )
        return remote_output

    def run(self, *args, cluster: Optional[Cluster] = None, **kwargs) -> RemoteObject:
        """
        Runs the function remotely on `self.cluster`

        Returns:
            RemoteObject: remote output dataclass containing reference to output
        """

        if GLOBAL_TASK_WRAPPER.get_task_wrapper() is None:
            print(
                "No GLOBAL_TASK_WRAPPER defined! Tasks should be run within context of a workflow"
            )
            self._wrapped_fn = self.remote
        else:
            self._wrapped_fn = GLOBAL_TASK_WRAPPER.get_task_wrapper().wrap(
                self.remote, self
            )

        return self._wrapped_fn(*args, cluster=cluster, **kwargs)


class FunctionTask(Task):
    def __init__(
        self,
        name: str,
        fn: Callable[[Any], Any],
    ):
        """
        Function Task object. This wraps a fn into a task

        Args:
            fn (Callable[[Any], Any]): callable function to be run
        """
        super().__init__(name)
        self.fn = fn

    def __call__(self, *args, **kwargs) -> Any:
        """
        Runs the fn with args & kwargs

        Returns:
            Any: function output
        """
        return self.fn(*args, **kwargs)


def task(
    fn: Callable[[Any], Any] = None,
    name: str = None,
    options: Optional[TaskOptions] = None,
    **kwargs,
):
    """
    Task decorator, returns a FunctiFunctionTaskon Task object

    Args:
        fn (Callable[[Any], Any]): callable function to be run
        name (str): name of the task
    """

    def decorator(fn):
        function_name = name
        if function_name is None:
            function_name = fn.__name__
        task = FunctionTask(name=name, fn=fn)
        return task

    if fn is None:
        return decorator

    function_name = name
    if function_name is None:
        function_name = fn.__name__

    task = FunctionTask(name=function_name, fn=fn)
    return task
