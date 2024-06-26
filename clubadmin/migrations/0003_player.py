# Generated by Django 3.2.25 on 2024-04-18 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubadmin', '0002_auto_20240416_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubadmin.team')),
            ],
        ),
    ]
