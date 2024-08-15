from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post, Category
from django.forms.widgets import DateTimeInput

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["text"].required = False

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'published_date': DateTimeInput(attrs={'type': 'datetime-local'}), 
            'created_date': DateTimeInput(attrs={'type': 'datetime-local'})}


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Category
        fields = '__all__'