from django.contrib import admin

from .models import Product, Category

#admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "id")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "id")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}