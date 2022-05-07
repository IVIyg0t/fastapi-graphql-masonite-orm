""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Company(Model):
    """Company Model"""

    @has_many("id", "company_id")
    def users(self):
        from models.db.User import User

        return User
