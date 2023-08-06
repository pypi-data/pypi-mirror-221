from typing import Any, Optional, Dict

from fastapi import HTTPException
from starlette import status

from switcore.action.schemas import SwitRequest


class NotFoundException(HTTPException):

    def __init__(self, detail: Any = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class NeedScopeException(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, str]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)
