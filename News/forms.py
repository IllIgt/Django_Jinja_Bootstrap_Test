from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
