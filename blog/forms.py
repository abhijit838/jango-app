"""
 Created by plank-abhijit on 14/1/17.
"""
from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
