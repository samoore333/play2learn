# Generated by Django 4.1.3 on 2023-02-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0028_alter_mathgame_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathgame',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
