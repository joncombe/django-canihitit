from django.contrib import admin
from .models import CanIHitIt


class CanIHitItAdmin(admin.ModelAdmin):
    list_display = ('object_type', 'object_id', 'session_key', 'created')
    list_filter = ('object_type', 'session_key')


admin.site.register(CanIHitIt, CanIHitItAdmin)
