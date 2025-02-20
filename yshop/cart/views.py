from django.shortcuts import render, redirect
from mainapp.models import Product
from .models import CartItem

# Create your views here.

# C - Creating cart items

def addToCart(request, product_id):
    this_product = Product.objects.get(id = product_id) # fetching the product object
    # When adding product to cart, we need to check if the same user has added the same product
    # to cart before, in that case, we will not create a new cart item, rather just increment 
    # quantity

    cart_item, created = CartItem.objects.get_or_create(product = this_product, user = request.user)
    cart_item.quantity += 1
    # above two statements are equivalent to `INSERT into table ... on duplicate key UPDATE ...` 
    cart_item.save() # save changes to SQL through Update

    return redirect('view_cart')

# R - Read Cartitems

def viewCart(request):
    template = 'cart.html'
    cart_items = CartItem.objects.filter(user = request.user) 
    # the above statement is equivalent to : SELECT * FROM cartitem WHERE user = <USER_ID>;
    total_price = sum(float(item.product.price) * item.quantity for item in cart_items)

    context = {
        'cart_items' : cart_items,
        'total_price' : total_price
    }
    return render( request, template, context)

