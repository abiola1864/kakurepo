from django.urls import path
from kakuapp.views import home, product_list, product_create, product_edit, product_delete, sale_list, sale_create, sale_edit, sale_delete

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/edit/', product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('sales/', sale_list, name='sale_list'),
    path('sales/create/', sale_create, name='sale_create'),
    path('sales/<int:pk>/edit/', sale_edit, name='sale_edit'),
    path('sales/<int:pk>/delete/', sale_delete, name='sale_delete'),
]
