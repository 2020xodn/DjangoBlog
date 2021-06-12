from django.contrib import admin
from .models import Posting, Photo, File


class PhotoInline(admin.TabularInline):
    model = Photo


class FileInline(admin.TabularInline):
    model = File


class PostingAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    inlines = [PhotoInline, FileInline]





admin.site.register(Posting, PostingAdmin)