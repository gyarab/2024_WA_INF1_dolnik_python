# Generated by Django 5.1.4 on 2025-01-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_category_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
