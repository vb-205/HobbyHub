from django import forms
from posts.models import Post

class PostBaseForm(forms.ModelForm):
        class Meta:
            model = Post
            exclude = ['author', 'group']
            widgets = {
                'title': forms.TextInput(attrs={
                    'placeholder': 'Enter post title'
                }),
                'description': forms.Textarea(attrs={
                    'placeholder': 'Write your description here...',
                    'rows': 6
                }),
            }

class CreatePostForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        ...