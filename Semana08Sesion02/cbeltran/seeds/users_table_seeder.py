from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert([{
            'name': 'cbeltran',
            'email': 'cbeltran.dev@outlook.com'
        },
        {
            'name': 'twittor',
            'email': 'twittor@twittor.com'
        },
        {
            'name': 'jose',
            'email': 'jose@email.com'
        },
        {
            'name': 'carlos',
            'email': 'carlos@email.com'
        },
        {
            'name': 'alvaro',
            'email': 'alvaro@email.com'
        }
        ])

