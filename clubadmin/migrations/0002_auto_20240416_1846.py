# Generated by Django 3.2.25 on 2024-04-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='newscategory',
            options={'verbose_name_plural': 'News Categories'},
        ),
    ]
