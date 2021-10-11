# Generated by Django 3.2.8 on 2021-10-11 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('number_of_players', models.IntegerField()),
                ('skill_level', models.CharField(max_length=100)),
                ('competitiveness_level', models.CharField(max_length=100)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.sport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
