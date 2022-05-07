from typing import List

import strawberry

from models.api.User import UserModel
from models.db.User import User as UserDB


@strawberry.experimental.pydantic.type(model=UserModel, all_fields=True)
class User:
    pass


@strawberry.type
class UsersQuery:
    @strawberry.field
    def user(self, info, id: int) -> User:
        return User(**UserDB.find_or_fail(id).serialize())

    @strawberry.field
    def users(self, info) -> List[User]:
        return [User(**user.serialize()) for user in UserDB.all()]
