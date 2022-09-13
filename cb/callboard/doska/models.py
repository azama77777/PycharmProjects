from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    objects = None
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Юзер')


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyer', 'Торговцы'),
        ('gm', 'Гильдмастеры'),
        ('qugiver', 'Квестгиверы'),
        ('bsmith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=12, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='uploads/')


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Massage(models.Model):
    pass


class Category(models.Model):
    pass
