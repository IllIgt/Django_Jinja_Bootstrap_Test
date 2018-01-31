from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from News.models import Articles
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                                template_name="News/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles,
                                             template_name='News/post.html')),
    url(r'^post/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]
