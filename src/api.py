from distutils.sysconfig import customize_compiler

import strawberry
from fastapi import Depends, FastAPI, Header
from strawberry.fastapi import GraphQLRouter

from src.middleware import validate_user
from src.queries.schema import Query
from src.routes import companies, posts, token, users


async def get_context(user=Depends(validate_user)):
    return dict(user=user)


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(companies.router)
app.include_router(token.router)


@app.get("/")
def read_root():
    return dict(msg="This is the news.")
