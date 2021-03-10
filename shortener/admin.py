from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('full_link', 'short_link', 'designed_link', 'count_use', 'created_date')
