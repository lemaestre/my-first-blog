from django.conf import settings
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField('Category', max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField('Title', max_length=200)
    head_image = CKEditor5Field('Cover Image', config_name='default', blank = True, null=True)
    caption = models.CharField('Caption', max_length=200, blank=True, null=True)
    text = CKEditor5Field('Body', config_name='extends')
    slug = models.SlugField(unique=True, null=True)
    snippet = models.TextField('Snippet', max_length=1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
