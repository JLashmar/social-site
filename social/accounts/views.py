from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login #login system
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView

from .models import Account

User = get_user_model()

class AccountDetailView(DetailView):
    template_name = 'accounts/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)
