# Generated by Django 4.1.3 on 2023-02-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagram', '0011_alter_anagramgame_word_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagramgame',
            name='word_length',
            field=models.IntegerField(default=5),
        ),
    ]