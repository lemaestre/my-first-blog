from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from taggit.models import Tag
from django.core.paginator import Paginator


# views here


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('draft_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/draft_list.html', {'posts': posts})


@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug)


@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('draft_list')


@login_required
def post_unpublish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.published_date=None
    post.save()
    return redirect('draft_list')


@login_required
def draft_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/draft_detail.html', {'post': post})


@login_required
def draft_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('draft_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/draft_edit.html', {'form': form})


def category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category, published_date__lte=timezone.now()).order_by('-published_date')  
    return render(request, 'blog/category_posts.html', {'posts':posts, 'category':category})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories':categories})


def search_feature(request):
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter model by the search query
        allposts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query) | Q(snippet__icontains=search_query) | Q(category__name__icontains=search_query) | Q(tags__name__icontains=search_query)).order_by('-created_date').distinct()
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query) | Q(snippet__icontains=search_query) | Q(category__name__icontains=search_query) | Q(tags__name__icontains=search_query), published_date__lte=timezone.now()).order_by('-published_date').distinct()
        return render(request, 'blog/search_results.html', {'query':search_query, 'liveposts':posts, 'adminposts':allposts})
    else:
        return render(request, 'blog/search_results.html',{})


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag, published_date__lte=timezone.now()).order_by('-published_date') 
    context = {'tag':tag, 'posts':posts,}
    return render(request, 'blog/tagged.html', context)