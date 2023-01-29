from django import forms
from django.forms import ModelForm
from .models import Comment
from .models import Post
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Create Submit Recipes Form


class SubmitForm(ModelForm):

    class Meta:
        model = Post
        fields = ("__all__")
