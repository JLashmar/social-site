from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.views import View

from .utils import unique_slug_generator

# Create your models here.

User = settings.AUTH_USER_MODEL

class Channel(models.Model):
    owner        = models.ForeignKey(User)
    name         = models.CharField(max_length=120)
    description  = models.TextField(max_length=150)
    timestamp    = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)
    category     = models.CharField(max_length=120)
    slug         = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('channels:detail', kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name

def channel_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

pre_save.connect(channel_pre_save_receiver, sender=Channel)
