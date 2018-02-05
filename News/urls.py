from django.conf.urls import url
from django.views.generic import ListView, DetailView
from News.models import Publications
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Publications,
                                             template_name ='News/publication_detail.html')),
    url(r'^$', views.index, name='publication_list'),
    url(r'^publication/(?P<pk>\d+)/$', views.post_detail, name='publication_detail'),
    url(r'^publication/new/$', views.post_new, name='publication_new'),
    url(r'^publication/(?P<pk>\d+)/edit/$', views.post_edit, name='publication_edit'),

]
