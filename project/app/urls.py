from app import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.user_login,name="user_login"),
]
