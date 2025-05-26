from django.contrib import admin
from .models import Category, Ad


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'condition')
    list_filter = ('category', 'condition')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image and f'<img src="{obj.image.url}" width="100">'

    image_preview.allow_tags = True