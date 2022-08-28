from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart, name="cart"),
    path("AddToCart/<int:x>", views.AddToCart, name="AddToCart"),
    path("remove/<int:x>", views.remove, name="remove"),
]
