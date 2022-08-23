from django.shortcuts import render, redirect, reverse
from products.models import Product, Category, SubCategory
# Create your views here.


def Product_list(req):
    pros = Product.objects.all()  # all / get field midi masalan name (try exept(None bashe error)) / filter (no error)
    print(pros[0].category.parent)
    if pros:
        pass
    return render(req, "Products/Product_list.html", {"Pros": pros})


def delete(req):
    return redirect(reverse("products:Product_list"))


def update(req):
    return redirect(reverse("products:Product_list"))
