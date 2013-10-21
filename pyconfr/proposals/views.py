
from django.views import generic
from pyconfr.proposals import models


class PosterListView(generic.ListView):
    model = models.PosterProposal
    template_name = 'proposals/poster_list.html'
    context_object_name = 'posters'


class PosterDetailView(generic.DetailView):
    model = models.PosterProposal
    template_name = 'schedule/presentation_detail.html'
    context_object_name = 'presentation'
