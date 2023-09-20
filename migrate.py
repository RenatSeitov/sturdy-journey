import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# Инициализируйте Django
django.setup()


import random
from faker import Faker
from django.utils import timezone

from movies.models import Genre, Movie


fake = Faker()

genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Science Fiction', 'Thriller']

for i in range(10):
    name = random.choice(genres)
    description = fake.paragraph()
    genre = Genre.objects.create(name=name, description=description)
    genre.save()

for i in range(20):
    title = fake.sentence()
    description = fake.paragraph()
    release_date = fake.date_between(start_date='-30y', end_date='today')
    price = round(random.uniform(1, 100), 2)
    genres = Genre.objects.order_by('?')[:random.randint(1, 3)]
    movie = Movie.objects.create(title=title, description=description, release_date=release_date, price=price)
    movie.genres.set(genres)
    movie.save()