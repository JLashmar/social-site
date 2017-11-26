from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from channels.models import Channel

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    channel = models.ForeignKey(Channel)
    #project stuff
    title            = models.CharField(max_length=120)
    description      = models.TextField(max_length=150)
    nsfw             = models.BooleanField(default=False)
    slug             = models.SlugField (max_length=120, blank=True, null=True)
    project_logo     = models.FileField()
    public           = models.BooleanField(default=True)
    timestamp        = models.DateTimeField(auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse('channels:index')
