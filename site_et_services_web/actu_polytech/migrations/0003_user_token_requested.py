# Generated by Django 4.2.3 on 2023-07-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actu_polytech', '0002_user_role_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token_requested',
            field=models.BooleanField(default=False),
        ),
    ]
