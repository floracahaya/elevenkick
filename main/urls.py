from django.urls import path
from .views import show_main, products_json, product_json_by_id, products_xml, product_xml_by_id
from .views import product_list, product_add, product_detail

app_name = 'main'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('main/', show_main, name='show_main'),
    path('add/', product_add, name='product_add'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('json/', products_json, name='products_json'),
    path('json/<int:pk>/', product_json_by_id, name='product_json_by_id'),
    path('xml/', products_xml, name='products_xml'),
    path('xml/<int:pk>/', product_xml_by_id, name='product_xml_by_id'),
]