# Generated by Django 4.1.3 on 2022-12-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0012_mathgame_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathgame',
            name='operation',
            field=models.CharField(choices=[('+', 'Addition'), ('-', 'Subtraction'), ('*', 'Multiplication'), ('/', 'Division')], default='+', max_length=20),
        ),
        migrations.AlterField(
            model_name='mathgame',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
