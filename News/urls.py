from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from News.models import Articles
from News import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
                                template_name="News/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles,
                                             template_name ='News/post.html')),
    url(r'^post/new/$', views.post_new, name='post_new')

]
