""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many


class Post(Model):
    """Post Model"""

    @belongs_to_many("post_id", "user_id", table="user_posts")
    def authors(self):
        from models.db.User import User

        return User
