# Generated by Django 5.0 on 2023-12-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='game_role',
            field=models.IntegerField(choices=[(0, 'civilian'), (1, 'werewolf'), (2, 'seer'), (3, 'innocent girl'), (4, 'hunter'), (5, 'cupido'), (6, 'witch'), (7, 'mayor'), (8, 'thief')], default=0),
        ),
    ]
