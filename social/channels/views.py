from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

# Create your views here.

from .models import Channel
from projects.models import Project
from .forms import ChannelCreateForm

class IndexView(ListView):
    queryset = Channel.objects.all()
    template_name = 'channels/channel-index.html'

class CategoryListView(ListView):
    template_name = 'channels/categoryview_list.html'

    def get_queryset(self):
        return Channel.objects.all()

class ChannelDetailView(DetailView):
    queryset = Channel.objects.all()

    def channel_projects(self):
        self.channel = get_object_or_404(Channel, slug=self.kwargs['slug'])
        return Project.objects.filter(channel=self.channel)

class ChannelCreateView(LoginRequiredMixin, CreateView):
    form_class = ChannelCreateForm
    template_name = 'form.html'
    #success_url = "/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(ChannelCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ChannelCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Channel'
        return context

class ChannelUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ChannelCreateForm
    template_name = 'form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ChannelUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update {name}'
        return context

    def get_queryset(self):
        return Channel.objects.filter(owner=self.request.user)
