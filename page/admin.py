from django.contrib import admin
from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'date_of_creation', 'date_of_editing', 'activity_flag')
    list_filter = ('name', 'content', 'date_of_creation', 'date_of_editing', 'activity_flag')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'text_comment', 'news')
    list_filter = ('username', 'text_comment', 'news')