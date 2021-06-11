from django.contrib import admin
from .models import Posting


class PostingAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Posting, PostingAdmin)