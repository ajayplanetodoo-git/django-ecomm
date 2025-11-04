from django.shortcuts import render , redirect
from django.http import HttpResponse, request
from .forms import ContactForm , LoginForm , RegisterForm
from django.contrib.auth import authenticate , login, logout
def home_pg(request):
    contxt = {
        'msg':'i have to make fully functional base ecormer-project',
        'content' : 'this is my home paget'
    }
    return render(request, 'index.html', contxt)

def about_pg(request):
    contxt = {
        'msg':'i have to make fully functional base ecormer-project',
        'content' : 'this is my about paget'
    }
    return render(request ,'index.html', contxt)

def contact_pg(request):
     contac_from = ContactForm(request.POST or None)
     contxt = {
        'msg':'i have to make fully functional base ecormer-project',
        'content' : 'this is my contact paget',
        'forms' : contac_from
    }
     if contac_from.is_valid():
         print("when every thing is corrected then this will store data ",contac_from.cleaned_data)
     if request.method=="POST":
         print(request.POST.get("fullname"))
         print(request.POST.get("email"))
     return render(request , 'contact/contact_views.html', contxt)

def login_pg(request):
    loginform = LoginForm( request.POST or None)
    contxt = {
        "forms":loginform
    }
    print(request.user.is_authenticated)
    if loginform.is_valid():   
        username = loginform.cleaned_data.get("username") # using clean_data from django forms is for the  validation,safty , type conversion
        password = loginform.cleaned_data.get("password") # if we use request.post.get("") it only for raw input it not do other thing like forms
        print("user input password and usename",loginform.cleaned_data)
        user = authenticate(request, username=username, password=password )
        
        if user is not None:
            login(request, user)
            # contxt['forms'] = LoginForm()
            return redirect("/login")
        else:
            print("error")
    return render(request, "auth/login.html", contxt)

def register_pg(request):
    registerform = RegisterForm(request.POST or None)
    contxt = {
        "forms":registerform
    }
    if registerform.is_valid:
        print(registerform.cleaned_data)
    return render(request, "auth/register.html", contxt)