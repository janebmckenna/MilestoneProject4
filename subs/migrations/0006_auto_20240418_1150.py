# Generated by Django 3.2.25 on 2024-04-18 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubadmin', '0003_player'),
        ('subs', '0005_auto_20240416_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_subs',
            name='player_name',
        ),
        migrations.AddField(
            model_name='team_subs',
            name='player',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='clubadmin.player'),
        ),
    ]
