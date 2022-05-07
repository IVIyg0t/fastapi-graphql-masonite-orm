""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many


class User(Model):
    """User Model"""

    __hidden__ = ["password"]

    @belongs_to_many("user_id", "post_id", table="user_posts")
    def posts(self):
        from models.db.Post import Post

        return Post
