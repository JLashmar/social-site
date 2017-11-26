from django.conf.urls import url, include
from django.urls import reverse_lazy

#my stuff

app_name = 'accounts'
#/user
urlpatterns = [
    url(r'^/', include('registration.backends.default.urls')),
]
