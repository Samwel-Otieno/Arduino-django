from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# User registration view
def Registerview(request):
    if (request.method=='POST'):
        user_form=RegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            messages.success(request, "Registration successful!!")
            return redirect("useraccounts:login")
    else:
        user_form=RegistrationForm()
    return render(request,'useraccounts/register.html', {'user_form':user_form})

#User login 
def login(request):
    if (request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)

        if user is not None:          
            auth.login(request,user)
            # send_mail(
            #     subject='User log',
            #     message= username +' logged in today',
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[user.email]
            #     )
            return render(request, 'webapp/index.html')
    else:
        return render(request, 'useraccounts/login.html')

#User logout 
def logout(request):
    auth.logout(request)
    return HttpResponse('Logged out Bye!')