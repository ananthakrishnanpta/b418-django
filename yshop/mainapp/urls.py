from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home, name='homepage'),
    path('products/', views.product_view, name='prod_page'),
    path('products/<int:id>', views.product_details, name='prod_details'),

    path('products/add', views.AddProduct.as_view(), name = 'add_prod'),

    path('products/edit/<int:pk>', views.EditProduct.as_view(), name = 'edit_prod'),

    path('products/del/<int:pk>', views.DelProduct.as_view(), name = 'del_prod'),
    path('products/search', views.searchView, name = 'prod_search')
]