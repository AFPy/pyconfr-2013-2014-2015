from django.conf.urls.defaults import *

from django.views.generic import list_detail


from pyconfr.proposals.models import PosterProposal
from pyconfr.proposals import views as posters_views


poster_info = {
    "queryset": PosterProposal.objects.all()
}

urlpatterns = patterns("",
    url(r"^$", posters_views.PosterListView.as_view(), name='poster_list'),
    url(r"^(?P<pk>\d+)/$", posters_views.PosterDetailView.as_view(),
        name='poster_detail'),
)
