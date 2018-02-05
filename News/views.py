from django.utils import timezone
from .models import Publications
from .forms import PublicationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def listing(request):
    contact_list = Publications.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('News/posts.html', {"contacts": contacts})

def post_list(request):
    posts = Publications.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'News/posts.html', {'publications': posts})


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
