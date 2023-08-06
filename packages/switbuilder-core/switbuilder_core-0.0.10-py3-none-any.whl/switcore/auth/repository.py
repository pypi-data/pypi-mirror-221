from sqlalchemy.orm import Session

from switcore.auth.exception import NotFoundException
from switcore.auth.models import User, App


class RepositoryBase:
    def __init__(self, session: Session):
        self.session = session


class AppRepository(RepositoryBase):
    def create(
            self,
            access_token: str,
            refresh_token: str,
            iss: str,
            apps_id: str,
            cmp_id: str | None
    ) -> App:
        token = App(
            access_token=access_token,
            refresh_token=refresh_token,
            iss=iss,
            apps_id=apps_id,
            cmp_id=cmp_id
        )
        self.session.add(token)
        self.session.commit()
        return token


class UserRepository(RepositoryBase):
    def create(self, swit_id: str, access_token: str, refresh_token: str) -> User:
        user = User(
            swit_id=swit_id,
            access_token=access_token,
            refresh_token=refresh_token
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get_or_create(self, swit_id: str, access_token: str, refresh_token: str):
        try:
            user = self.get_by_swit_id(swit_id=swit_id)
        except NotFoundException:
            user = self.create(
                swit_id=swit_id,
                access_token=access_token,
                refresh_token=refresh_token
            )
        return user

    def get_by_swit_id(self, swit_id: str) -> User:
        """
        :raises UserNotFoundException:
        """
        user_or_null: User | None = self.session.query(User).filter(User.swit_id == swit_id).first()
        if user_or_null is None:
            raise NotFoundException(detail="User not found")
        return user_or_null

    def update_token(self, swit_id: str, access_token: str, refresh_token: str) -> User:
        user = self.get_by_swit_id(swit_id=swit_id)
        user.access_token = access_token
        user.refresh_token = refresh_token
        self.session.commit()
        return user

    def delete(self, swit_id: str) -> None:
        user = self.get_by_swit_id(swit_id)
        self.session.delete(user)
        self.session.commit()
