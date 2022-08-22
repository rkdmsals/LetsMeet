from django.shortcuts import render
from django.contrib.auth import logout

def sociallogin(request):
    return render(request, 'sociallogin/sociallogin.html')


def logout_view(request):
    logout(request)
    return render(request, 'sociallogin/logout.html')

# def register_view(request):
#     return 
