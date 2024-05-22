from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
        if request.method == "POST":
            First_name = request.POST['first_name']
            Last_name = request.POST['last_name']
            Username = request.POST['username']
            Password1 = request.POST['password1']
            Password2 = request.POST['password2']
            Email = request.POST['email']

            if Password1 == Password2:
                if User.objects.filter(username=Username).exists():
                    messages.info(request, "username is already taken")
                    return redirect("register")

                elif User.objects.filter(email=Email).exists():
                    messages.info(request, "email is already taken")
                    return redirect("register")

                else:
                    user = User.objects.create_user(username=Username, password=Password1, email=Email,first_name=First_name, last_name=Last_name)
                    user.save()
                    print("user created")
            else:
                print("password not correct")
                return redirect('register')

            return redirect('/')

        else:
            return render(request,'register.html')
        

def login(request):
        if request.method=='POST':
            Username=request.POST['username']
            Password=request.POST['password1']
            user=auth.authenticate(username=Username,password=Password)


            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'invalid details')
                return redirect('login')

        else:
            return render(request,'login.html')        

def logout(request):
    auth.logout(request)
    return redirect('/')