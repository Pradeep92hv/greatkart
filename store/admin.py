from django.contrib import admin

# Register your models here.


from .models import Product,variation
class ProductAdmin(admin.ModelAdmin):
# class ProductAdmin(models.ModelAdmin):
    list_display=('product_name','price','stock','category','modified','is_available')
    prepopulated_fields={'slug':('product_name',)}
    

class variationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable=('is_active',)
    list_filter=('product','variation_category','variation_value','is_active')
     


admin.site.register(Product,ProductAdmin)
admin.site.register(variation,variationAdmin)