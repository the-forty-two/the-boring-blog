from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views as api_view


urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^api/$', api_view.PostList.as_view()),
    url(r'^(?P<slug>[-\w]+)/$', views.post, name='post'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.posts_by_category, name='post_by_category'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
