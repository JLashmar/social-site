from django import forms
from channels.models import Channel
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'channel',
            'title',
            'description',
            'nsfw',
            #'slug',
            'public',
            #'project_logo',
        ]

    def __init__(self, user=None, *args, **kwargs):
        #print(kwargs.pop('user'))
        print(user)
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['channel'].queryset = Channel.objects.filter(owner=user)
