from django.shortcuts import render, redirect
from products.models import Product, SubCategory


def Product_list(req):
    # pros = Product.objects.all()  # all / get field midi masalan name (try exept(None bashe error)) / filter (no error)
    pros = Product.objects.filter(deleted=False)
    return render(req, "Products/Product_list.html", {"Pros": pros})


def delete(req, x):
    # todo:
    # 2 → image bakhsh edit ham hamintor dorostesh kon
    try:
        mahsol = Product.objects.get(id=x)
        # mahsol.delete()
        mahsol.deleted = True
        mahsol.save()
        return redirect("products:list")
    except Product.DoesNotExist:
        return redirect("products:list")


def update(req, x):
    mahsol = Product.objects.get(id=x)
    SubCategories = SubCategory.objects.all()
    if req.method == "GET":
        return render(req, "Products/edit.html", {"Pros": mahsol, "SubCategories": SubCategories})
    mahsol.name = req.POST.get("name", False)
    mahsol.price = req.POST.get("price", False)
    mahsol.count = req.POST.get("count", False)
    mahsol.description = req.POST.get("description", False)
    mahsol.image = req.POST.get("image", False)
    category = req.POST.get("SubCategory", False)
    mahsol.category = SubCategory.objects.get(name=category)
    mahsol.is_active = req.POST.get("is_active", False)
    mahsol.save()
    return redirect("products:list")


def details(req, x):
    try:
        mahsol = Product.objects.get(id=x)
        return render(req, "Products/detail.html", {"Pros": mahsol})
    except Product.DoesNotExist:
        return redirect("products:list")


# if req.user.has_perm('foo.view_bar'):
#     return HttpResponse("ok")
