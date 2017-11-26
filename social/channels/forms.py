from django import forms
from .models import Channel

class ChannelCreateForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = [
            'name',
            'description',
            'category',
        ]

    def validate_name(self):
        name = self.cleaned_data.get('name')
        if name == 'Hello':
            raise forms.ValidationError('Not a valid name')
        return name
