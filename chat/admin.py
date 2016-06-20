from django.contrib import admin
from .models import Theme, Comment


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme', 'text',)  # 一覧に出したい項目
    list_display_links = ('theme', 'text', )  # 修正リンクでクリックできる項目
admin.site.register(Theme, ThemeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('themeid', 'comment',)  # 一覧に出したい項目
    list_display_links = ('comment', )  # 修正リンクでクリックできる項目
admin.site.register(Comment, CommentAdmin)