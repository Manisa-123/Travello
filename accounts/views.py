from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, UserManager, auth
from django.urls import reverse
from django.contrib import messages
from travello.models import Destination

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else :    
        template = loader.get_template('login.html')
        return HttpResponse(template.render({},request))


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
       

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Registered")
                return redirect('register')
            else :
                user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save();
                return redirect('login')
                
            # HttpResponseRedirect(reverse('index.html'))
        else:
            messages.info(request,"Passwords MisMatching")
            return redirect('register')
        return redirect('/')

    else:
        template = loader.get_template('register.html')
        return HttpResponse(template.render({},request))

def spots(request, id):
    
    if request.user.is_authenticated : 
        dest=Destination.objects.get(id=id)
        template = loader.get_template('spots.html')
        context={
        'dest' : dest,
         }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('/')
