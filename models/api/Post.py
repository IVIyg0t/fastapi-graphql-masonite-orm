from models.api.Base import BaseModel


class PostModel(BaseModel):
    title: str
    content: str
    user_posts_id: int | None = None
