from django.urls import path
from . import views


urlpatterns = [
    path('sayHI/', views.sayHI),
]

