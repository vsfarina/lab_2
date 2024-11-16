from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
