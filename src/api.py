from fastapi import FastAPI

from src.routes import companies, posts, token, users

app = FastAPI()
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(companies.router)
app.include_router(token.router)


@app.get("/")
def read_root():
    return dict(msg="This is the news.")
