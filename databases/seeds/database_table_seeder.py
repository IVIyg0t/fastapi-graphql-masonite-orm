"""DatabaseTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from databases.seeds.company_table_seeder import CompanyTableSeeder

from .post_table_seeder import PostTableSeeder
from .user_table_seeder import UserTableSeeder


class DatabaseTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(PostTableSeeder)
        self.call(UserTableSeeder)
        self.call(CompanyTableSeeder)
