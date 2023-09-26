from django.contrib import admin

from products.models import Basket, Product, ProductCategory

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity', 'category')
	filds = ('name', 'description', 'price', 'quantity', 'image', 'category')
	readonly_fields = ('descriptiom',)
	search_fields = ('name',)
	ordering = ('name',)


class BasketAdmin(admin.TabularInline):
	model = Basket
	field = ('product', 'quantity')
	extra = 0