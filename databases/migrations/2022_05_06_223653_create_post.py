"""CreatePost Migration."""

from masoniteorm.migrations import Migration


class CreatePost(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.string("title")
            table.text("content")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
