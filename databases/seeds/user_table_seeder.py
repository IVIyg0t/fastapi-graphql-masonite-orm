"""UserTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from models.db.Post import Post
from models.db.User import User
from src.middleware import get_password_hash


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            dict(
                firstname="Taylor",
                lastname="Roberts",
                username="myg0t",
                email="fake@gmail.com",
                password=get_password_hash("pass"),
                disabled=False,
                company_id=1,
            )
        )

        User.find(1).attach("posts", Post.find(1))
