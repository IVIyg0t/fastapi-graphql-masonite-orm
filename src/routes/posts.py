from typing import Optional

from fastapi import APIRouter

from models.db.Post import Post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
def get_post():
    return Post.all().serialize()


@router.post("/")
def create_post(title: str, content: str):
    post = Post()
    post.title = title
    post.content = content
    post.save()

    return post.id


@router.put("/{id}")
def update_post(id: int, title: Optional[str] = None, content: Optional[str] = None):
    post = Post.find(id)

    post.title = title or post.title
    post.content = content or post.content

    post.save()

    return post.serialize()


@router.get("/{id}")
def get_post(id: int):
    return Post.find(id).serialize()


@router.get("/{id}/authors")
def get_post_authors(id: int):
    return Post.find(id).authors.serialize()
