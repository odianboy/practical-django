from django.db import models


class News(models.Model):
    STATUS_ACTIVITY = [
        ('a', 'Actively'),
        ('n', 'Not active')

    ]
    name = models.CharField(max_length=255, verbose_name='Название')
    content = models.CharField(max_length=255, verbose_name='Содержание')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_of_editing = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    activity_flag = models.BooleanField(default=True, verbose_name='Флаг активности')
    status = models.CharField(max_length=1, choices=STATUS_ACTIVITY, default='a')

    def __str__(self):
        return f'{self.id}. {self.name}'


class Comment(models.Model):
    STATUS_ACT = [
        ('d', 'Remotely'),
        ('a', 'Acting')

    ]
    username = models.CharField(max_length=20, verbose_name='Имя пользователя')
    text_comment = models.CharField(max_length=255, verbose_name='Текст коментария')
    news = models.ForeignKey('News', related_name='news',
                             default=None, null=True, on_delete=models.CASCADE, verbose_name='Новость')
    act = models.CharField(max_length=1, choices=STATUS_ACT, default='a')

    def __str__(self):
        return f'{self.id}. {self.username}'
