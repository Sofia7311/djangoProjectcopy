from django.urls import path
from . import views


urlpatterns = [
    path("login",views.loginPage,name="loginPage"),
    path("register",views.register,name="register"),
    path("logout",views.logout_view,name="logout"),

]