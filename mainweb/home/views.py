from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def design(request):
    return render(request, 'home/homedesign.html')