# Generated by Django 3.0 on 2022-03-27 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('date', models.DateField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game', verbose_name='Авто')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='Пользователь')),
            ],
        ),
    ]