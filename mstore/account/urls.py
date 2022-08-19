from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.log_out, name="logout"),
    path('profile/', views.profile, name="profile"),
]
