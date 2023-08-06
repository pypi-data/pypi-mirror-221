import inspect
from typing import Optional, Union

from trainyard.engine import ClusterSpec, RemoteObject, cluster, set_default_backend
from trainyard.tasks import Task, TaskOptions, task, task_options
from trainyard.track import Track


def options(options: Optional[TaskOptions] = None, **kwargs) -> Union[Task, Track]:
    def dec(task_or_track):
        if inspect.isclass(task_or_track):
            if issubclass(task_or_track, Task):
                return task_options(options, **kwargs)(task_or_track)
        if isinstance(task_or_track, Task):
            return task_options(options, **kwargs)(task_or_track)

    return dec


__all__ = [
    "Task",
    "task",
    "Track",
    "TaskOptions",
    "options",
    "ClusterSpec",
    "RemoteObject",
    "cluster",
    "set_default_backend",
]
