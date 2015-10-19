from django import http
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Poll
from .forms import PollForm


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class OwnerRequiredMixin(object):
    owner_field = 'user'

    def is_owner(self, request, *args, **kwargs):
        self.object = self.get_object()
        return getattr(self.object, self.owner_field, None) == request.user

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        if self.is_owner(request, *args, **kwargs) or request.user.is_superuser:
            return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()


class PollDetailView(OwnerRequiredMixin, DetailView):
    model = Poll
    template_name = 'simplepoll/poll_detail.html'
    context_object_name = 'poll'


class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    template_name = 'simplepoll/poll_create.html'
    form_class = PollForm

    def get(self, request, *args, **kwargs):
        if Poll.objects.filter(user=self.request.user).exists():
            pollofuser = Poll.objects.get(user=self.request.user)
	    return HttpResponseRedirect(reverse_lazy('poll_update', kwargs={'pk':pollofuser.pk}))
        else:
            return super(PollCreateView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PollCreateView, self).form_valid(form)



class PollUpdateView(OwnerRequiredMixin, UpdateView):
    model = Poll
    template_name = 'simplepoll/poll_update.html'
    form_class = PollForm
