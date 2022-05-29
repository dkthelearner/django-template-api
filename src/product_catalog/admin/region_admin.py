from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from import_export.admin import ImportExportModelAdmin

from ..models import Region


@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.PositiveIntegerField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100, 'style': 'resize:none;'})},
    }
    fieldsets = (
        ("Region Form", {
            'fields': (
                'name',
                'description',
                'display_order',
                'is_approved'
            ),
        }),
    )
    list_display = (
        'region_id', 'image', 'name', 'description',
        'display_order', 'is_approved', 'created_at', 'updated_at'
    )
    list_select_related = ('image',)
    list_display_links = ('region_id', 'image',)
    list_filter = ('created_at', 'updated_at', 'name')
    search_fields = ('region_id', 'name',)
    autocomplete_fields = ('image',)
    ordering = ('-updated_at',)
