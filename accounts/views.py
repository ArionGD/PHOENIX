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
            # Redirect based on role (Admin vs User)
            if user.role == 'admin' or user.is_staff:
                return redirect('dashboard_admin:overview')
            else:
                return redirect('user:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'accounts/login.html')
