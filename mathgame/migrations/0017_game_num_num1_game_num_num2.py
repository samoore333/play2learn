# Generated by Django 4.1.3 on 2023-01-04 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0016_remove_game_num_num1_remove_game_num_num2'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_num',
            name='num1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='game_num',
            name='num2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
