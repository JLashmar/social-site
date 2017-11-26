from django.conf.urls import url, include
from django.urls import reverse_lazy

#my stuff
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView

app_name = 'projects'
#/user
urlpatterns = [
    url(r'^$', ProjectListView.as_view(), name='home'),
    url(r'^create/$', ProjectCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit$', ProjectUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='detail'),
]
