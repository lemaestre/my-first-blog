from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post, Comment

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["text"].required = False

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text')
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}),
            'text': forms.Textarea(
                attrs={'class':'form-control','placeholder': 'Comments are moderated.'})}
        

