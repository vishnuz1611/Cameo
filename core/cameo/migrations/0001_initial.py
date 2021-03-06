# Generated by Django 3.2.8 on 2021-12-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('rated', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MovieSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Year', models.CharField(blank=True, max_length=5)),
                ('Plot', models.CharField(max_length=1000)),
                ('Lang', models.CharField(blank=True, max_length=100)),
                ('Poster', models.ImageField(upload_to='cameo')),
                ('Poster_url', models.URLField(blank=True)),
                ('Type', models.CharField(blank=True, max_length=100)),
                ('Seasons', models.CharField(blank=True, max_length=3)),
                ('imdbRating', models.CharField(blank=True, max_length=5)),
                ('imdbID', models.CharField(blank=True, max_length=100)),
                ('Genre', models.ManyToManyField(blank=True, to='cameo.Genre')),
                ('Ratings', models.ManyToManyField(to='cameo.Rating')),
            ],
        ),
    ]
