from typing import List

import strawberry

from models.api.Post import PostModel
from models.db.User import User as UserDB


@strawberry.experimental.pydantic.type(model=PostModel, all_fields=True)
class Post:
    pass


@strawberry.type
class PostsQuery:
    @strawberry.field
    def my_posts(self, info) -> List[Post]:
        user = info.context["user"]
        return [Post(**post.serialize()) for post in user.posts.all()]
