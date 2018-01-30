from django.shortcuts import render
from django import forms


def post_new(request):
    form = Form()
    return render(request, 'News/posts.html', {'form': form})
