# Generated by Django 3.2.25 on 2024-04-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0006_auto_20240412_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
