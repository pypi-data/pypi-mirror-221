from fastapi import HTTPException
from starlette import status

from switcore.action.schemas import SwitRequest


class SwitUserNotFoundException(HTTPException):
    def __init__(self, detail: str, swit_request):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
        self.swit_request: SwitRequest = swit_request


class SwitNeedScopeException(HTTPException):
    def __init__(self, detail: str, swit_request):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
        self.swit_request: SwitRequest = swit_request
