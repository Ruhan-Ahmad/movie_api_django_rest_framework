from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_no']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Movies(models.Model):
    movie_name = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=500)
    long_desc = models.CharField(max_length=3000)
    thumbnail_url = models.URLField(max_length=500)
    movie_url = models.URLField(max_length=500)
    genre = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.movie_name


class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.movie_name


