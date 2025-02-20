from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.viewCart, name='view_cart'),
    path('add/<int:product_id>', views.addToCart, name='add_to_cart')
]