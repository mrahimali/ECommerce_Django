from django.contrib import admin
from .models import *


class AdminProduct(admin.ModelAdmin):
    list_display=['name', 'price', 'category']


admin.site.register(Product, AdminProduct)

# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display=['id','name']


# admin.site.register(Category)
admin.site.register(Category, AdminCategory)
# admin.site.register(Product)


class AdminCutomer(admin.ModelAdmin):
    list_display=['first_name','last_name']

admin.site.register(Cutomer, AdminCutomer)

