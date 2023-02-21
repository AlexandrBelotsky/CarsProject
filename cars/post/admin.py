from django.contrib import admin

from post.models import Cars, Category


class ACars(admin.ModelAdmin):
    list_display = ('brand', 'slug', 'image', 'description', 'price', 'update', 'published', 'category')
    list_display_links = ('brand', 'description')
    search_fields = ('brand', 'description')
    prepopulated_fields = {'slug': ('brand',)}


class ACategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ['name',]}


admin.site.register(Cars, ACars)
admin.site.register(Category, ACategory)


