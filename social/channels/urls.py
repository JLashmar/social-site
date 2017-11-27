from django.conf.urls import url, include
from django.urls import reverse_lazy

#my stuff
from channels.views import IndexView, CategoryListView, ChannelDetailView, ChannelCreateView, ChannelUpdateView

app_name = 'channels'
#/user
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^channel/create/$', ChannelCreateView.as_view(), name='create'),
    url(r'^channel/(?P<slug>[\w-]+)/edit$', ChannelUpdateView.as_view(), name='edit'),
    url(r'^channel/(?P<slug>[\w-]+)/$', ChannelDetailView.as_view(), name='detail'),
    url(r'^category/(?P<category>\w+)/$', CategoryListView.as_view(), name='category'),
]
