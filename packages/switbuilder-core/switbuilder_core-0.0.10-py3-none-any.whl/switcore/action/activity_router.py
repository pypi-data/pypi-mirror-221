from collections import defaultdict

from switcore.type import DrawerHandler


def escape(text: str) -> str:
    return text.replace('/', '\\')


class PathResolver:
    def __init__(self, id: str, paths: list[int | str] | None = None) -> None:
        if paths is None:
            paths = []

        self._id: str = escape(id)
        self._paths: list[str] = []
        for path in paths:
            self.add_path(path)

    def __str__(self):
        return self.combined_path

    @property
    def combined_path(self) -> str:
        path: str = '/'.join(self._paths)
        return f'{self._id}/{path}'

    @property
    def id(self) -> str:
        return self._id

    @property
    def paths(self) -> list[int | str]:
        ret: list[int | str] = []
        for path in self._paths:
            if path.isdigit():
                ret.append(int(path))
            else:
                ret.append(path)

        return ret

    @staticmethod
    def from_combined(combined_id: str) -> 'PathResolver':
        arr: list[str] = combined_id.split('/')
        paths: list[str] = arr[1:]

        if len(paths) == 1 and paths[0] == '':
            paths = []

        return PathResolver(arr[0], paths)

    def add_path(self, path: int | str):
        assert isinstance(path, int) or isinstance(path, str), "only int or str is allowed"

        if isinstance(path, int):
            path = str(path)

        self._paths.append(escape(path))


class ActivityRouter:

    def __init__(self) -> None:
        self.handler: dict[str, dict[str, DrawerHandler]] = defaultdict(dict)
        self.action_ids_to_be_called_in_views: set[str] = set()

    def register(self, action_id: str, view_ids: list[str] | None = None):
        if view_ids is None:
            view_ids = ['*']

        def decorator(func):
            for view_id in view_ids:
                _action_id = escape(action_id)
                self.action_ids_to_be_called_in_views.add(_action_id)
                self.handler[escape(view_id)][_action_id] = func
            return func

        return decorator
