# Generated by Django 4.1.3 on 2022-12-14 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0002_rename_mathscore_mathgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathgame',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathgame',
            name='max_number',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathgame',
            name='operation',
            field=models.CharField(choices=[('+', '+'), ('-', '-'), ('*', 'x'), ('/', '/')], default='+', max_length=1),
        ),
        migrations.AddField(
            model_name='mathgame',
            name='score',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
