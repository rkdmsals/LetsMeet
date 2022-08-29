from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def redirect_to_user_profile(request):
    if request.user.is_authenticated:
        print(request.user.pk)
        redirect_url = f"{request.user.pk}/"
        return HttpResponseRedirect(redirect_to=redirect_url)

# Create your views here.
@login_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile_view.html')


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'users/profile_view.html')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)

        return render(request, 'users/profile_update.html', {'user_change_form':user_change_form})
