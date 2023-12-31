# Generated by Django 5.0 on 2023-12-15 13:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_role', models.IntegerField(choices=[(0, 'civilian'), (1, 'werewolf'), (2, 'seer'), (3, 'innocent girl'), (4, 'hunter'), (5, 'cupido'), (6, 'witch'), (7, 'mayor'), (8, 'thief')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
