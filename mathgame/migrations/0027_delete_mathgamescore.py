# Generated by Django 4.1.3 on 2023-02-16 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0026_rename_score_mathgamescore_scores_mathgame_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MathgameScore',
        ),
    ]