from django.shortcuts import render, HttpResponse
from home.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from rest_framework.authtoken.models import Token
from django.http import HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed


# Create your views here.
def checkAuthRequest(request):
    if request.method == "GET":
        parameter = request.GET.get('token', '')
        if parameter != "":
            isValidToken = Token.objects.filter(key=parameter)
            if isValidToken:
                return HttpResponse("1")
            else:
                return HttpResponseForbidden()
        else:
            return HttpResponseBadRequest()
    return HttpResponseNotAllowed()
    



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        passsword = request.POST['password']
        response = checkCredentials(username, passsword)
        try:
            Token.objects.filter(user_id=User.objects.filter(Q(username=username))[0]).delete()
            showToken(response)
            return HttpResponse("generated token")
        except:
            return render(request, "Login.html")
    else:
        return render(request,"Login.html")

def checkCredentials(username, passe):
    querry = User.objects.filter(Q(username=username))
    for i in querry:
        if (check_password(passe, i.password)):
            return i
    return "Wrong credentials"


def authStudent(request):
    pass


def userExists(match):
    querry = User.objects.filter(Q(username = match))
    if len(querry) > 0:
        return True
    return False


def emailExists(match):
    querry = User.objects.filter(Q(email = match))
    if len(querry) > 0:
        return True
    return False

def showToken(request):
    token = Token.objects.create(user=request)
    return HttpResponse(token.key)

def addUser(request):
    if request.method == "GET":
        return render(request, "addUser.html")
    else:
        if not userExists(request.POST["username"]):
            if not emailExists(request.POST["email"]):
                instance = User(
                    username = request.POST["username"],
                    password = make_password(request.POST["password"]),
                    email = request.POST["email"],
                    first_name = request.POST["first_name"],
                    last_name = request.POST["last_name"],
                )
                instance.save()
                return render(request, "userAuthenticated.html")
            else:
                return HttpResponse("E-mail already used!")
        else:
            return HttpResponse("User already exists!")
