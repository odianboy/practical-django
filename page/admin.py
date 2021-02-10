from django.contrib import admin
from .models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_creation', 'activity_flag', 'status')
    list_filter = ('activity_flag', )
    search_fields = ('name', 'content')
    inlines = [CommentInLine]

    actions = ['mark_activity', 'mark_not_activity']

    def mark_activity(self, request, queryset):
        queryset.update(status='a')

    def mark_not_activity(self, request, queryset):
        queryset.update(status='n')

    mark_activity.short_description = 'Перевести в стаптус Активно'
    mark_not_activity.short_description = 'Перевести в стаптус Не активно'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'list_text_comment', 'news', 'act')
    list_filter = ('username', 'text_comment', 'news')
    search_fields = ('username', )

    actions = ['mark_remotely', 'mark_acting']

    def mark_remotely(self, request, queryset):
        queryset.update(act='d')

    def mark_acting(self, request, queryset):
        queryset.update(act='a')

    mark_remotely.short_description = 'Удалено администратором'
    mark_acting.short_description = 'Действуюший комментарий'

#   TODO Пофиксиь выдачу теста из за произведенного дейвтвия

    def list_text_comment(self, obj):
        if CommentAdmin.mark_acting:
            return f'{obj.text_comment[:15]}...'
        elif CommentAdmin.mark_remotely:
            return 'Удалено администратором'

    list_text_comment.short_description = 'text'
