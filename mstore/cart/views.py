from django.shortcuts import render, redirect
from products.models import Product
from cart.models import Cart


def cart(req):
    cart_pros = Cart.objects.all()
    return render(req, "cart/cart.html", {"Pros": cart_pros})


def AddToCart(req, x):
    mahsol = Product.objects.get(id=x)
    z = Cart.objects.create(id_mahsol=mahsol.id)
    z.save()
    return redirect("products:list")


def remove(req, x):
    mahsol = Product.objects.get(id=x)

    mahsol.delete()
    return render(req, "cart/cart.html", {"Pros": mahsol})
