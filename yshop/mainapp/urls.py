from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('products/<int:id>', views.product_details, name='prod_details')
]