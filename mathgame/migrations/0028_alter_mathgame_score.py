# Generated by Django 4.1.3 on 2023-02-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathgame', '0027_delete_mathgamescore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathgame',
            name='score',
            field=models.CharField(default=0, max_length=20),
        ),
    ]