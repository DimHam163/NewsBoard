from django.contrib import admin
from board.models import Announcement, Comment, Category


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'publish']
    list_filter = ['created', 'author', 'publish']
    search_fields = ['title', 'text']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'announcement', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

