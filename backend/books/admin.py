from django.contrib import admin
from .models import Book, Subject, Year

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'subject', 'is_public', 'upload_date']
    list_filter = ['year', 'subject', 'is_public', 'upload_date']
    search_fields = ['title', 'author']
    list_editable = ['is_public']