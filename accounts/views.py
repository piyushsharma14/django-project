from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password

def signup(request):
    if request.method == 'POST':
        if request.POST['psw'] == request.POST['psw-repeat']:
            try:
                user =User.objects.get(username= request.POST['email'])
                return render(request, 'register.html',{'error':"Email has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username= request.POST['email'], first_name= request.POST['first'], last_name=request.POST['last'], password= request.POST['psw'], email= request.POST['email'])
                return redirect(login)
        else:
            return render(request,'register.html', {'error':"Password Don't Match"})
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['psw']

        user = auth.authenticate(username=email, password=pwd)

        if user is not None:
           auth.login(request,user)
           return render(request,'index.html')
        else:
            return render(request,'login.html',{'error': "Invalid Credentials"})

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect(login)