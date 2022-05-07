import strawberry

from src.queries.posts import PostsQuery
from src.queries.users import UsersQuery


@strawberry.type
class Query(UsersQuery, PostsQuery):
    pass
