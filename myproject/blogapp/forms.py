from django import forms

from .models import Author


class AuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name', 'email', 'biography', 'birthday']