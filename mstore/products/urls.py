from django.urls import path
from . import views

app_name = "products"


urlpatterns = [
    path('', views.Product_list),
    # path('Product_list/<int:X>', views.Product_list, name="Product_list"),
    path('delete/<int:X>', views.Product_list, name="delete"),
    path('update/<int:X>', views.Product_list, name="update"),
]
