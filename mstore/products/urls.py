from django.urls import path
from . import views

app_name = "products"


urlpatterns = [
    path('', views.Product_list, name="list"),
    path('details/<int:x>', views.details, name="details"),
    path('delete/<int:x>', views.delete, name="delete"),
    path('update/<int:x>', views.update, name="update"),
]
