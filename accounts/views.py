from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('accounts:register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('login')
                print("User Created")
        else:
            print("password not matched")
            return redirect('accounts:register')
        return redirect('/')

    return render(request, 'register.html')
def loginn(request):
    return render(request,'login.html')
