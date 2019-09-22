from django.shortcuts import render
from .models import Post, Comment
from blog.forms import CommentForm
# Create your views here.

# displays a list of all posts.


def blog_index(request):
    # - sign indicates to start with largest value.
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }

    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category).order_by('-created_on')
    context = {
        'posts': posts,
        'selected_category': category
    }

    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog_detail.html', context)
