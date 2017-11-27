from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

# Create your views here.

from .models import Channel
from accounts.models import Account
from projects.models import Project
from .forms import ChannelCreateForm

class ChannelFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        #print(request.data)
        #print(request.POST)
        user_to_toggle = request.POST.get('user')
        print(user_to_toggle)
        account_ = Account.objects.get(user__username__iexact=user_to_toggle)
        user = request.user
        if user in account_.followers.all():
            account_.followers.remove(user)
        else:
            account_.followers.add(user)
        return redirect('/')

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
