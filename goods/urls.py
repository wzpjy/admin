from django.urls import path
from . import views

app_name = "goods"

urlpatterns = [

    path('home', views.home, name="home"),

    path('Category_Manage', views.Category_Manage, name="Category_Manage"),

    path('picture_add/<int:type_id>', views.picture_add, name="picture_add"),

    path('Products_List', views.Products_List, name="Products_List"),

    path('Brand_Manage', views.Brand_Manage, name="Brand_Manage"),

    path('add_page', views.add_page, name="add_page"),

    path('product_category_add/<int:pid>', views.product_category_add, name="product_category_add"),

    path('upload_product', views.upload_product, name="upload"),

    path('category_tree', views.category_tree, name="category-tree"),
]
