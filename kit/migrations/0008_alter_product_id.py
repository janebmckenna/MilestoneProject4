# Generated by Django 3.2.25 on 2024-04-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0007_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
