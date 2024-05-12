from django.conf import settings
from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
from django.db.models import Q



class Category(models.Model):
    name = models.CharField('Category', max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField('Title', max_length=200)
    head_image = CKEditor5Field('Cover Image', config_name='default', blank = True, null=True)
    text = CKEditor5Field('Body', config_name='extends')
    tags = TaggableManager(blank=True)
    slug = models.SlugField(unique=True, null=True)
    snippet = models.TextField('Snippet', max_length=1000, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField('Publish date', blank=True, null=True)


    class Meta:
        ordering = ('-published_date',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date=None
        self.save()

    def __str__(self):
        return self.title
    
    @classmethod #filter object
    def published(cls):
        return cls.objects.filter(published_date__lte=timezone.now())
    
    @classmethod #filter objects
    def draft(cls):
        return cls.objects.filter(published_date__isnull=True)
    
    @classmethod #filter objects
    def scheduled(cls):
        return cls.objects.exclude(Q (published_date__lte=timezone.now()) | Q(published_date__isnull=True))
    
    @property #per one object access in template
    def is_draft(self):
        return self.published_date > timezone.now() or self.published_date==None
    