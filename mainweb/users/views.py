from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

# Create your views here.
class ProfileView(DetailView):
    context_object_name = 'profile_user' 
    model = User
    template_name = 'users/profile.html' #


class ProfileUpdateView(request):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        user_form = UserForm(initial={
            'email': user.email,
        })

        if hasattr(user, 'profile'):
            profile=user.profile
            profile_form=ProfileForm(initial={
                'nickname':profile.nickname,
                'photo':profile.photo,
                'intro':profile.intro,
                'phone':profile.phone
            })
        else:
            profile_form=ProfileForm()
        return render(request, 'user/profile_update.html', {"user_form":user_form, "profile_form":profile_form})