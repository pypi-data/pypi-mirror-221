from httpx import AsyncClient, Auth as HttpxAuth
from httpx_oauth.oauth2 import RefreshTokenError
from sqlalchemy.orm import Session
from starlette import status

from switcore.auth.exception import NeedScopeException
from switcore.auth.oauth2 import OAuth2
from switcore.auth.repository import UserRepository
from switcore.auth.schemas import SwitToken
from switcore.logger import get_logger


def get_http_client() -> AsyncClient:
    return AsyncClient(
        auth=Auth()
    )


class Auth(HttpxAuth):

    def __init__(
            self,
            swit_oauth2: OAuth2,
            swit_id: str,
            access_token: str,
            refresh_token: str,
            session: Session
    ):
        self.swit_oauth2 = swit_oauth2
        self.swit_id = swit_id
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.session = session

    async def async_auth_flow(self, request):
        logger = get_logger()
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        response = yield request
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            user_repository = UserRepository(self.session)
            try:
                new_token: SwitToken = await self.swit_oauth2.refresh_token(self.refresh_token)
                user_repository.update_token(self.swit_id, new_token.access_token, new_token.refresh_token)
            except RefreshTokenError as exc:
                logger.error(str(exc))
                user_repository.delete(self.swit_id)

            request.headers["Authorization"] = f"Bearer {self.access_token}"
            yield request
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            raise NeedScopeException("Need scope")
