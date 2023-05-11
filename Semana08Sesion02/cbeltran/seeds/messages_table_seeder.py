from orator.seeds import Seeder


class MessagesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        user = self.db.table('users').where('name', 'cbeltran').first()

        self.db.table('messages').insert({
            'content': 'Este es un mensaje',
            'user_id': user['id']
        })

