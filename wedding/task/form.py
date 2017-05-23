from django.forms import ModelForm, Textarea,TextInput
from django import forms
from django.contrib.auth.models import Permission, Group
from .models import Todo_list

  
 
class Todo_listForm(ModelForm): 
    class Meta:
        model = Todo_list
        fields = ['title', 'description']
        exclude = ['date', 'publisher','finish_date', 'finisher', 'status']
