# Generated by Django 5.1.4 on 2025-04-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_game_votes_count_game_votes_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='games/image'),
        ),
    ]
