"""PostTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from models.db.Post import Post


class PostTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        Post.create(
            dict(
                title="Stan's First Post",
                content="All my life I seem to be in the wrong place at the wrong time. My grandfather, Stanley Yelnats II says it's because of a 150-year family curse. Well, I don't believe in the family curse, but when things go wrong, it kinda helps to be able to blame it on something. And for me... things went wrong a lot. Grandpa says our destiny's sealed. Could a pair of shoes falling from the sky be part of my destiny? You see my father, Stanley Yelnats III, is an inventor, and for the last few years, he's been trying to find a cure... for foot odour",
            )
        )
