from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'discription', 'cat_image')
    prepopulated_fields = {'slug': ('category_name',)}

# Register the Category model with the CategoryAdmin class
admin.site.register(Category, CategoryAdmin)
