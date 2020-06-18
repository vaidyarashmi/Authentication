from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import User_DetailsForm
# Create your views here.
def Login_Page(request):
    print(request.POST)
    if request.method=='POST':

        Username = request.POST['Username']
        Password = request.POST['Password']
        request.session['Username']=Username
        try:
           user = User_Details.objects.get(Username=Username)
           if Username == user.Username and Password == user.Password:
               u=User_Details.objects.all()
               return render(request,"Profile.html",{'u':u,'user':Username})
           else:
               return render(request, "login.html")
        except User_Details.DoesNotExist:
               return render(request, "SignUp.html")
    else:
        return render(request, "login.html")

def profile(request):
    u=User_Details.objects.all()
    return render(request,"Profile.html",{'u':u})

def destroy(request, id):
    u = User_Details.objects.get(User_ID=id)
    u.delete()
    alluser=User_Details.objects.all()
    return render(request,"Profile.html",{'u':alluser})

def signup(request):
    if request.method=="POST":
        print(request.POST)
        Username=request.POST['Username']
        Password = request.POST['Password']
        user=User_Details(Username=Username,Password=Password)
        user.save()
        return render(request,"login.html")
    else:
        return render(request,"SignUp.html")

def logout(request):
   del request.session['Username']
   return render(request,"login.html")
