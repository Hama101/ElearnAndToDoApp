from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    CHOICES = [
        ( True ,"Done" ),
        ( False , "Not Yet" )
    ]
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    done = forms.BooleanField(required=False ,widget= forms.CheckboxInput(attrs={'class':'checkbox'}))
    class Meta:
        model = Item
        fields = '__all__'