from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from goods.models import TGoodsType, DjangoMigrations, TGoods, DjangoMigrations
from .forms import GoodsModelForm
from django.conf import settings
import os, uuid


def home(request):
    return render(request, "home.html")


def Category_Manage(request):
    return render(request, "Category_Manage.html")


def Products_List(request):
    data = TGoods.objects.order_by("-create_time")

    return render(request, "Products_List.html", {"data": data})


def Brand_Manage(request):
    return render(request, "Brand_Manage.html")


def add_page(request):
    type_id = request.session.pop("type_id", '')

    return render(request, "picture-add.html", {"type_id": type_id})


def picture_add(request, type_id):
    if request.method == "GET":
        print(type_id, "get")
        return render(request, "picture-add.html", {"id": type_id})
    if request.method == "POST":
        print(type_id, "post")
        # 接受页面传过来的参数
        param = request.POST.dict()
        img_url = request.POST.getlist("img_url")
        param.pop("img_url")
        param.pop("file")
        # 将参数写入表中
        param["sort_id"] = type_id
        print(param, img_url)
        product = TGoods.objects.create(**param)

        for i in img_url:
            DjangoMigrations.objects.create(image=i, product_id=product.id)
        return render(request, "picture-add.html")


def upload_product(request):
    # 获取文件上传的对象
    file = request.FILES.get("file")

    file_name = uuid.uuid4().hex + file.name

    file_path = os.path.join(settings.MEDIA_ROOT, 'product', file_name)

    with open(file_path, "wb") as f:
        for chunk in file.chunks():
            f.write(chunk)

    return JsonResponse(data={"img_url": "product/" + file_name})


def product_category_add(request, pid):
    if request.method == "GET":
        return render(request, "product_category_add.html", {"pid": pid})
    # 添加分类
    param = request.POST.dict()
    # 将 pid 添加到数据中
    param["pid_id"] = pid
    param["status"] = 1
    goods_type = TGoodsType.objects.create(**param)
    return JsonResponse(model_to_dict(goods_type))


def category_tree(request):
    category = TGoodsType.objects.order_by("orderby").filter(status=1).values("id", "type_name", "pid")

    return JsonResponse(list(category), safe=False, json_dumps_params={"ensure_ascii": False})
