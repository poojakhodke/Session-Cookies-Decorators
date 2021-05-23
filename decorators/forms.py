from django import forms
from django.contrib.auth.models import User
from decorators.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'slug', 'content', 'created_by')

