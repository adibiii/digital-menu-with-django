from django.contrib import admin

from lorca.models import Category, Item


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'fname', 'description', 'is_active')


@admin.register(Item)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'fname', 'description', 'price', 'category', 'is_active')
    list_filter = ('category',)
