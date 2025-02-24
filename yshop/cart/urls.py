from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.viewCart, name='view_cart'),
    path('add/<int:product_id>', views.addToCart, name='add_to_cart'),
    path('del/<int:cart_item_id>', views.removeFromCart, name='del_cart'),

    # The following url patterns will be requested by the JS function
    path('cart/add/<int:cart_item_id>/', views.add_quantity, name='add_quantity'),
    path('cart/remove/<int:cart_item_id>/', views.remove_quantity, name='remove_quantity'),
]