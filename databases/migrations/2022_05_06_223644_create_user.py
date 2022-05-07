"""CreateUser Migration."""

from masoniteorm.migrations import Migration


class CreateUser(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")
            table.string("firstname")
            table.string("lastname")
            table.string("username")
            table.string("email").unique()
            table.string("password")
            table.boolean("disabled")
            table.integer("company_id").unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
