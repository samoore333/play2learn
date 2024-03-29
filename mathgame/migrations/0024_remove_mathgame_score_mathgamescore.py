# Generated by Django 4.1.3 on 2023-01-23 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mathgame', '0023_alter_mathgame_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mathgame',
            name='score',
        ),
        migrations.CreateModel(
            name='MathgameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('mathgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mathgamescore', to='mathgame.mathgame')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mathgamescore', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
