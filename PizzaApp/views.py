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
    return render(request,"login.html")
    
def menu(request):
    return render(request,"menu.html")

def order(request):
    return render(request,"order.html")

def rewards(request):
    return render(request,"rewards.html")
