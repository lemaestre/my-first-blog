from .forms import PostForm
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from taggit.models import Tag
from django.core.paginator import Paginator
from django.views.generic.list import ListView



def home(request):
    recent = Post.published()[0:4]
    categories = Category.objects.all()
    context = {'recent':recent,'categories':categories}
    return render (request, 'blog/home.html',context)

def post_list(request):
    posts = Post.published()
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('draft_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

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
    drafts = (Post.draft() | Post.scheduled()).order_by('-created_date')
    return render(request, 'blog/draft_list.html', {'drafts': drafts})

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
    post.unpublish()
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
    posts = Post.objects.filter(category=category) & Post.published()
    context = {'posts':posts, 'category':category}
    return render(request, 'blog/category_posts.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories':categories})

def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        allposts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query) | Q(snippet__icontains=search_query) | Q(category__name__icontains=search_query) | Q(tags__name__icontains=search_query)).order_by('-created_date').distinct()
        liveposts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query) | Q(snippet__icontains=search_query) | Q(category__name__icontains=search_query) | Q(tags__name__icontains=search_query), published_date__lte=timezone.now()).distinct()
        context = {'query':search_query, 'live':liveposts, 'admin':allposts}
        return render(request, 'blog/search_results.html', context)
    else:
        return render(request, 'blog/search_results.html',{})

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug) 
    posts = Post.objects.filter(tags=tag) & Post.published()
    context = {'tag':tag, 'posts':posts,}
    return render(request, 'blog/tagged.html', context)
