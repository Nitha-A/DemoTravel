from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, "invalid username or password")
            return redirect("login")
    else:

         return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        password= request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=secondname,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password doesnot match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")