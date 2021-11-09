# create forms.py in category app, add CategoryForm
# make create_category method
# add url
# add html

from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)