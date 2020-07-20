from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")


def Category_Manage(request):
    return render(request, "Category_Manage.html")


def Products_List(request):
    return render(request, "Products_List.html")


def Brand_Manage(request):
    return render(request, "Brand_Manage.html")


def product_category_add(request):
    return render(request, "product_category_add.html")
