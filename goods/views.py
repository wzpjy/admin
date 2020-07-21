from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from goods.models import TGoodsType


def home(request):
    return render(request, "home.html")


def Category_Manage(request):
    return render(request, "Category_Manage.html")


def Products_List(request):
    return render(request, "Products_List.html")


def Brand_Manage(request):
    return render(request, "Brand_Manage.html")


def product_category_add(request, pid):
    if request.method == "GET":
        return render(request, "product_category_add.html", {"pid": pid})
    # 添加分类
    param = request.POST.dict()
    # 将 pid 添加到数据中
    param["pid"] = pid
    param["status"] = 1
    goods_type = TGoodsType.objects.create(**param)
    return JsonResponse(model_to_dict(goods_type))


def category_tree(request):
    category = TGoodsType.objects.order_by("orderby").filter(status=1).values("id", "type_name", "pid")

    return JsonResponse(list(category), safe=False, json_dumps_params={"ensure_ascii": False})
