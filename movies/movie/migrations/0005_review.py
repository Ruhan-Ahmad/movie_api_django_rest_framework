# Generated by Django 4.1.5 on 2023-01-16 08:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movies_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='anonymous', max_length=40)),
                ('review_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(max_length=4000)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movies')),
            ],
        ),
    ]