from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    POST_TYPES = (
        ('NW', 'Новость'),
        ('AR', 'Статья'),
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_type = models.CharField(max_length=2, choices=POST_TYPES, verbose_name='Тип записи')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title