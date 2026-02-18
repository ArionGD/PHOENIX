from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.role in ['manager', 'superuser']:
                return redirect('manager_dashboard:overview')
            else:
                return redirect('user_dashboard:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'accounts/login.html')
