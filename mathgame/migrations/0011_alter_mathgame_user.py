# Generated by Django 4.1.3 on 2022-12-29 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mathgame', '0010_alter_mathgame_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathgame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
