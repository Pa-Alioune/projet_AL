from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from news.models import Article, Category


class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **options):
        categories = ['Sport', 'Santé', 'Education', 'Politique']
        for category in categories:
            Category.objects.create(name=category)

        # Creating a new user
        User = get_user_model()
        # user = User.objects.create_user('rone1', 'user1@example.com', 'rone1passer')
        # Replace 'existing_username' with the actual username
        user = User.objects.get(username='rone1')

        sport = Category.objects.get(name='Sport')
        politique = Category.objects.get(name='Politique')
        education = Category.objects.get(name='Education')

        Article.objects.create(title="Inauguration d'un ENO à l'UVS",
                               content='Lorem ipsum...',
                               category=education,
                               author=user)
        Article.objects.create(title="Bac 2023",
                               content='Lorem ipsum...',
                               category=education,
                               author=user)
        Article.objects.create(title="BFEM 2023",
                               content='Lorem ipsum...',
                               category=education,
                               author=user)
        Article.objects.create(title="CFEE   2023",
                               content='Lorem ipsum...',
                               category=education,
                               author=user)

        Article.objects.create(title='Deuxiéme victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Troisieme victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Quatrieme victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Cinquiéme victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)
        Article.objects.create(title='Sixiéme victoire du Sénégal',
                               content='Lorem ipsum...',
                               category=sport,
                               author=user)

        Article.objects.create(title='Election au Senegal',
                               content='Lorem ipsum...',
                               category=politique,
                               author=user)

        Article.objects.create(title='Election en Gambie',
                               content='Lorem ipsum...',
                               category=politique,
                               author=user)
        Article.objects.create(title='Election en France',
                               content='Lorem ipsum...',
                               category=politique,
                               author=user)

        self.stdout.write(self.style.SUCCESS(
            'Database populated successfully'))
