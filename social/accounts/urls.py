from django.conf.urls import url, include
from django.urls import reverse_lazy

from accounts.views import AccountDetailView

app_name = 'accounts'
#/user
urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', AccountDetailView.as_view(), name='detail'),
    url(r'^/', include('registration.backends.default.urls')),
]
