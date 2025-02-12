from django.shortcuts import render, redirect 
from django.http import HttpResponse

from django.template import loader 
from .models import Product # importing the Product class from models.py

# Create your views here.
def home(request):
    context = {
        'current_page' : 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def product_view(request): 
    products = Product.objects.all() # querying all records in the DB of entity type `Product`
    # i.e. this translates to the DQL :-> `SELECT * FROM PRODUCT;`
    # the `products` variable now contains a collection of all `Product` class objects.
    context = {
        'prods' : products, # the key `prods` will now be available to use in the django template design 
        'current_page' : 'products'

    } # context dictionary for passing data for rendering 
    template = loader.get_template('products.html') # creating a template object from the designed template html
    return HttpResponse(template.render(context, request)) # creates a response object after rendering
    # the returned response has the html of completed webpage including required data.

# view function for rendering individual product page 
def product_details(request, id):
    product = Product.objects.get(id = id) # select * from products where id = <parameter_id>
    context = {
        'prod' : product,
        'current_page' : 'products'
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))