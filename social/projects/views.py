from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import ProjectForm
from .models import Project

class ProjectListView(ListView):
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user) #Project.objects.filter(channel=1)

class ProjectDetailView(DetailView):
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProjectCreateView, self). form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ProjectForm

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Project'
        return context

    def get_form_kwargs(self):
        kwargs = super(ProjectUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
