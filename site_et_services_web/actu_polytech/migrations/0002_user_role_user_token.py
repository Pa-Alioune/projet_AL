# Generated by Django 4.2.3 on 2023-07-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actu_polytech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]