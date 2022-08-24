from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import auth

from .models import Moim


# Create your views here.

class MoimListView(generic.ListView):
    model = Moim

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(MoimListView, self).get_context_data(**kwargs)
        context['users_list'] = Moim.objects.all() # 수정 .. 필요
        return context



class MoimDetailView(generic.DetailView):
    model = Moim

    # def moim_detail_view(request, primary_key):
    #     moim = get_object_or_404(Moim, pk=primary_key)
    #     return render(request, 'organizations/moim_detail.html', context={'moim': moim})
    

class MoimCreateView(generic.CreateView):
    model = Moim
    fields = ('name', 'detail', 'join_users', 'start_date', 'end_date')

    success_url = "/organizations/list"
    # Once the creation success, the user is redirected to success_url. 
    # We can also define a method get_success_url instead and use reverse or reverse_lazy to get the success url.
