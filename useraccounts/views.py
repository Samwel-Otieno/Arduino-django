from django.shortcuts import render

# Create your views here.

# User registration view
def register(request):
    return render(request, 'useraccounts/register.html')

#User login 
def login(request):
    return render(request, 'useraccounts/login.html')

#User logout 
def logout(request):
    return render(request, 'useraccounts/logout.html')