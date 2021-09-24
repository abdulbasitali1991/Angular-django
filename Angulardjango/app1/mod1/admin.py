from typing import Callable
from django.contrib import admin
from .models import Product,ProductSize,ProductSite,Comments,Category,Company
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','content')
    list_filter = ('category', )
    




admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Company)
admin.site.register(Comments)
admin.site.register(Category)


admin.site.site_header= "product Review Admin"
