from django.contrib import admin
from hobby_groups.models import HobbyGroup


@admin.register(HobbyGroup)
class HobbyGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at')  # customize to your fields
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)