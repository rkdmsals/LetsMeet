from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Moim

# Create your views here.

class MoimListView(generic.ListView):
    model = Moim

    def get_context_data(self, **kwargs):
        context = super(MoimListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data' 
        return context



class MoimDetailView(generic.DetailView):
    model = Moim

    def moim_detail_view(request, primary_key):
        moim = get_object_or_404(Moim, pk=primary_key)
        return render(request, 'organizations/moim_detail.html', context={'moim': moim})
