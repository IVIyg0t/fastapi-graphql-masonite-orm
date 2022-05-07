"""CreateUserPost Migration."""

from masoniteorm.migrations import Migration


class CreateUserPost(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_posts") as table:
            table.increments("id")
            table.integer("user_id").unsigned()
            table.integer("post_id").unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_posts")
