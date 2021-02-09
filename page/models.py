from django.db import models


class News(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    content = models.CharField(max_length=255, verbose_name='Содержание')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_of_editing = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    activity_flag = models.CharField(max_length=20, verbose_name='Флаг активности')

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.CharField(max_length=20, verbose_name='Имя пользователя')
    text_comment = models.CharField(max_length=255, verbose_name='Текст коментария')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE, verbose_name='Новость')

    def __str__(self):
        return self.username
