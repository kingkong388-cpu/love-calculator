from django.contrib import admin
from .models import Couple
from django.utils.html import format_html

@admin.register(Couple)
class CoupleAdmin(admin.ModelAdmin):
    list_display = ('name_a', 'name_b', 'percent', 'score', 'created_at', 'photo_a_tag', 'photo_b_tag')
    
    # Add methods to show image thumbnails
    def photo_a_tag(self, obj):
        if obj.photo_a:
            return format_html('<img src="{}" width="50" />', obj.photo_a.url)
        return "-"
    photo_a_tag.short_description = 'Photo A'

    def photo_b_tag(self, obj):
        if obj.photo_b:
            return format_html('<img src="{}" width="50" />', obj.photo_b.url)
        return "-"
    photo_b_tag.short_description = 'Photo B'
