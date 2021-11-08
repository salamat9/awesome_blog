from django import forms
from categories.models import Category


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    description = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())


