from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def destinations(request):
    return render(request, 'destinations.html')

def packages(request):
    return render(request, 'packages.html')

def package1(request):
    return render(request, 'package1.html')

def delhi(request):
    return render(request, 'delhi.html')

def kerala(request):
    return render(request, 'kerala.html')

def malaysia(request):
    return render(request, 'malaysia.html')

def punjab(request):
    return render(request, 'punjab.html')

def rajasthan(request):
    return render(request, 'rajasthan.html')

def singapore(request):
    return render(request, 'singapore.html')

def thailand(request):
    return render(request, 'thailand.html')

def varanasi(request):
    return render(request, 'varanasi.html')
