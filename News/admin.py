from django.contrib import admin
from News.models import Articles
from .models import Post

admin.site.register(Post)
admin.site.register(Articles)
