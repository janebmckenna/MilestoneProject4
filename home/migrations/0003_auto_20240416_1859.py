# Generated by Django 3.2.25 on 2024-04-16 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_news_category_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='News_Category',
        ),
    ]
