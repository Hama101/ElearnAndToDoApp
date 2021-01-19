from django import forms
from django.forms import ModelForm

from .models import *
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    done = forms.BooleanField(required=False ,widget= forms.CheckboxInput(attrs={'class':'checkbox'}))
    date = forms.DateTimeField(widget=forms.DateInput())

    class Meta:
        model = Item
        fields = '__all__'


class CoursesFrom(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Course...'}))
    imgUrl = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Image...'}))
    ytUrl = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new YouTube link...'}))
    description = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new Description...'}))
    done = forms.BooleanField(required=False ,widget= forms.CheckboxInput(attrs={'class':'checkbox'}))
    class Meta:
        model = Course
        fields = '__all__'