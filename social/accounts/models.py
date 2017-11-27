from django.db import models
from django.conf import settings #base user model
from django.db.models.signals import post_save

from channels.models import Channel

User = settings.AUTH_USER_MODEL



class Account(models.Model):
    user         = models.OneToOneField(User) #user.profile
    followers     = models.ManyToManyField(Channel, related_name='is_following', blank=True) #user.is_following.all() ((who I am following))
    #following    = models.ManyToManyField(User, related_name='following', blank=True) #user.is_following.all() ((my followers))
    activated    = models.BooleanField(default=False)
    #Personal Info
    first_name   = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    bio          = models.TextField(max_length=500, blank=True)
    birth_date   = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

def post_save_user_reciever(sender, instance, created, *args, **kwargs):
    if created:
        account, is_created = Account.objects.get_or_create(user=instance)
        default_user_account = Account.objects.get(user__id=1)

post_save.connect(post_save_user_reciever, sender=User)


#for making them automatically follow me
#default_user_account = Account.objects.get(user__id=1)
