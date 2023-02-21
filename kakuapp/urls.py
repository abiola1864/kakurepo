from django.urls import path
from kakuapp.views import product_list, product_create, product_edit, product_delete, sale_list, sale_create, sale_edit, sale_delete, home

urlpatterns = [
    path('', home, name='home'),
    path('product/', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('sale/', sale_list, name='sale_list'),
    path('sale/create/', sale_create, name='sale_create'),
    path('sale/<int:pk>/edit/', sale_edit, name='sale_edit'),
    path('sale/<int:pk>/delete/', sale_delete, name='sale_delete'),
]
