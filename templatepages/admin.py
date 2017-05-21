from django.contrib import admin

from templatepages.models import Image, TemplateVar

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'alt_text')

@admin.register(TemplateVar)
class TemplateVarAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')

