# Generated by Django 4.0.1 on 2022-02-02 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_numofrec_game_participants'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game_numOfP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOfP', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
        ),
    ]
