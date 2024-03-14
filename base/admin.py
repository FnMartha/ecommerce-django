from django.contrib import admin
from .models import Product, Review, Order, Orderitem, ShippingAddress

# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(ShippingAddress)
