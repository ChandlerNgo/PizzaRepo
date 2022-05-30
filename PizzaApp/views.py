from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        response = {
            "loginstate":"Log Out",
        }
        return render(request,"index.html",response)
    else:
        response = {
            "loginstate":"Log In",
        }
        return render(request,"index.html",response)

def login(request):
    if request.user.is_authenticated:
        response = {
            "loginstate":"Log Out",
        }
        return render(request,"login.html",response)
    else:
        response = {
            "loginstate":"Log In",
        }
        return render(request,"login.html",response)

def order(request):
    return render(request,"order.html")

def rewards(request):
    return render(request,"rewards.html")

def createaccount(request):
    return render(request,"createaccount.html")

def forgotpassword(request):
    return render(request,"forgotpassword.html")

def termsandconditions(request):
    return render(request,"termsandconditions.html")
