from django.shortcuts import render, HttpResponse
from home.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Q

# Create your views here.


def authStudent(request):
    pass


def userExists(match):
    querry = User.objects.filter(Q(username=match))
    if len(querry) > 0:
        return True
    return False


def emailExists(match):
    querry = User.objects.filter(Q(email=match))
    if len(querry) > 0:
        return True
    return False


def addUser(request):
    if request.method == "GET":
        return render(request, "addUser.html")
    else:
        if not userExists(request.POST["username"]):
            if not emailExists(request.POST["email"]):
                instance = User(
                    username=request.POST["username"],
                    password=make_password(request.POST["password"]),
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                )
                instance.save()
                return render(request, "userAuthenticated.html")
            else:
                return HttpResponse("E-mail already used!")
        else:
            return HttpResponse("User already exists!")
