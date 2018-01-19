from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('blogview:post_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category)
    title = models. CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(max_length=10000)
    seo_title = models.CharField(max_length=200)
    seo_description = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='blog_post')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    music_link = models.CharField(max_length=300, default='')

    def get_absolute_url(self):
        return reverse('blogview:post', args=[self.slug])

    def __str__(self):
        return self.title

