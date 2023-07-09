from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from news.models import Article, Category


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        categories = ['Sport', 'Santé', 'Education', 'Politique']


        # Creating a new user
        User = get_user_model()
        # user = User.objects.create_user('rone1', 'user1@example.com', 'rone1passer')
        user = User.objects.get(username='rone1')  # Replace 'existing_username' with the actual username

        sport = Category.objects.get(name='Sport')
        politique = Category.objects.get(name='Politique')
        education = Category.objects.get(name='Education')

        Article.objects.create(title='Première victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Election en Mauritanie',
                               content='Lorem ipsum...',
                               category=politique,
                               author=user)
        Article.objects.create(title='Début de la CAN',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Pétrole au Sénégal',
                               content='Lorem ipsum...',
                               category=politique,
                               author=user)
        Article.objects.create(title="Inauguration d'un ENO à l'UVS",
                               content='Lorem ipsum...',
                               category=education,
                               author=user)

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
