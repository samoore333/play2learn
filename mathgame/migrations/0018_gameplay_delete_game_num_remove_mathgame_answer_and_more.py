# Generated by Django 4.1.3 on 2023-01-04 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mathgame', '0017_game_num_num1_game_num_num2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gameplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField(blank=True, null=True)),
                ('num2', models.IntegerField(blank=True, null=True)),
                ('correct_answer', models.IntegerField(blank=True, null=True)),
                ('incorrect_answer', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
                ('time_left', models.IntegerField(default=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Game_num',
        ),
        migrations.RemoveField(
            model_name='mathgame',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='mathgame',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='mathgame',
            name='score',
        ),
        migrations.RemoveField(
            model_name='mathgame',
            name='time_left',
        ),
        migrations.AddField(
            model_name='gameplay',
            name='mathgame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplays', to='mathgame.mathgame'),
        ),
        migrations.AddField(
            model_name='gameplay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameplays', to=settings.AUTH_USER_MODEL),
        ),
    ]
