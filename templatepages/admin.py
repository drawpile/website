from django.contrib import admin

from templatepages.models import Documentation, Image, TemplateVar

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'alt_text')

@admin.register(TemplateVar)
class TemplateVarAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')

@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'permission')
