"""CreateCompany Migration."""

from masoniteorm.migrations import Migration


class CreateCompany(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("companies") as table:
            table.increments("id")
            table.string("name")
            table.string("address")
            table.string("city")
            table.string("state")
            table.string("phone")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("companies")
