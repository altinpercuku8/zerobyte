from django import forms
from .models import Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['thread_title', 'thread_content']