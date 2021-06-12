from django.contrib import admin
from .models import Posting, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class PostingAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    inlines = [PhotoInline, ]


admin.site.register(Posting, PostingAdmin)







