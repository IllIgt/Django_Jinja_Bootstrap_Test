from django.utils import timezone
from .models import Publications
from .forms import PublicationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def post_list(request):
    posts = Publications.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'News/publication_list.html', {'publications': posts})


def post_new(request):
    if request.method == "POST":
        form = PublicationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('publication_detail', pk=post.pk)
    else:
        form = PublicationForm()
    return render(request, 'News/publication_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Publications, pk=pk)
    return render(request, 'News/publication_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Publications, pk=pk)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('publication_detail', pk=post.pk)
    else:
        form = PublicationForm(instance=post)
    return render(request, 'News/publication_edit.html', {'form': form})
