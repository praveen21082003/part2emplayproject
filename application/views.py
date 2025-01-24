from django.shortcuts import render, redirect
from application.models import *
from application.forms import *
from django.contrib.auth import authenticate, login
from application.forms import loginForm

def input_view(request):
    r=registerForm()
    if request.method == 'POST':
        r=registerForm(request.POST)
        if r.is_valid():
            r.save(commit=True)
    return render(request,'htmlpages/register.html',{'form':r})



def loginview(request):
    r = loginForm()  
    # Initialize the login form
    if request.method == 'POST':  
        # Getting the form data from the request
        r = loginForm(request.POST)  
        if r.is_valid():  
            # Getting the cleaned data
            email = r.cleaned_data.get('email')
            password = r.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None: 
                login(request, user) 
                return redirect('htmlpages/profile.html')
            else:
                return render(request, 'htmlpages/profile.html', {'form': r, 'error': 'Invalid credentials'})  # Display error message

    return render(request, 'htmlpages/login.html', {'form': r})



