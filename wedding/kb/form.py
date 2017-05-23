from django.forms import ModelForm, Textarea,TextInput
from django import forms

class UploadImageForm(forms.Form):
	imagefile 	= forms.FileField()

