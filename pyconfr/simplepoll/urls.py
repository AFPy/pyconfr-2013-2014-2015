from django.conf.urls.defaults import *
from .views import PollDetailView, PollCreateView, PollUpdateView


urlpatterns = patterns(
    "",
    url(r"^simplepolldetail/(?P<pk>\d+)/$", PollDetailView.as_view(), name="poll_detail"),
    url(r"^simplepollcreate/$", PollCreateView.as_view(), name="poll_create"),
    url(r"^simplepollupdate/(?P<pk>\d+)/$", PollUpdateView.as_view(), name="poll_update"),
)
