from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('adminuser/', admin.site.urls),
    url(r'^', include('mainApp.urls')),
    url(r'^news/', include('News.urls')),
    url(r'publication/', include('News.urls')),

]
