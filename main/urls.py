from django.urls import path
from .views import show_main, product_list, product_add, product_detail
from .views import products_json, product_json_by_id, products_xml, product_xml_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),  # ini yang harusnya jadi halaman utama
    path('products/', product_list, name='product_list'),
    path('products/add/', product_add, name='product_add'),
    path('products/<int:pk>/', product_detail, name='product_detail'),

    # API endpoints
    path('json/', products_json, name='products_json'),
    path('json/<int:pk>/', product_json_by_id, name='product_json_by_id'),
    path('xml/', products_xml, name='products_xml'),
    path('xml/<int:pk>/', product_xml_by_id, name='product_xml_by_id'),
]
