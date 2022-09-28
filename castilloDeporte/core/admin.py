from unicodedata import category
from django.contrib import admin
from . models import Product, Category, Client, Cart

#admin.site.register(Product)
admin.site.register(Category)
#admin.site.register(Client)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'image', 'category')
    list_display = ["name","price","slug","created_ad"]
    #list_display_links = ("name", "price")
    list_editable = ["price"]
    search_fields = ["name"]
    #list_filter = ["category"]
    list_per_page = 10

admin.site.register(Cart)