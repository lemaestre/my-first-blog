from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["text"].required = False

    class Meta:
        model = Post
        fields = '__all__'