# Generated by Django 4.1.3 on 2023-01-31 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagram', '0003_anagramgame_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anagramgame',
            old_name='end_time',
            new_name='created',
        ),
        migrations.AddField(
            model_name='anagramgame',
            name='category',
            field=models.CharField(default='Anagram Hunt', max_length=50),
        ),
        migrations.AddField(
            model_name='anagramgame',
            name='slug',
            field=models.SlugField(default=12345, editable=False, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anagramgame',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='anagramgame',
            name='word_length',
            field=models.IntegerField(default=5),
        ),
    ]
