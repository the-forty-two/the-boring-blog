from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.posts_by_category, name='post_by_category'),
]