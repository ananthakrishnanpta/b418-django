from django.contrib import admin
from .models import Product
# Register your models here.


admin.site.register(Product) # this registers the access of `Product` class model into admin panel