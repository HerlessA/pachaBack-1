from orator.seeds import Seeder


class UsersTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        # pasando datos a alimentar
        self.db.table("users").insert(
            {"name": "twittor", "email": "twittor@twittor.com"}
        )
        self.db.table("users").insert({"name": "john", "email": "john@doe.com"})
        self.db.table("users").insert({"name": "jane", "email": "jane@doe.com"})
