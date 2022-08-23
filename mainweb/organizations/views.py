from django.shortcuts import render, get_object_or_404
from django.views import generic

from mainweb.organizations.models import Moim

# Create your views here.

class MoimDetailView(generic.DetailView):
    model = Moim

    def moim_detail_view(request, primary_key):
        moim = get_object_or_404(Moim, pk=primary_key)
        return render(request, 'organizations/moim_detail.html', context={'moim': moim})
