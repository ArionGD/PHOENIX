from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def support(request):
    return render(request, 'core/support.html')

def feature(request):
    return render(request, 'core/feature.html')
