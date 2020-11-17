from django.urls import path, include
from home.views import *

urlpatterns = [
    path("addUser", addUser),
    path("showToken", showToken),
    path("Login", login),
    path("checkAuth", checkAuthRequest)
]
