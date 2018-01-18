from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def posts_by_category(request, category_slug):
    categories = Category.objects.all()
    posts = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    template = 'posts_by_category.html'
    context = {'categories': categories, 'posts': all_posts, 'category': category}
    return render(request, template, context)


def blog(request):
    all_post = Post.objects.filter(status='published')
    paginator = Paginator(all_post, 2)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    template = 'all_posts.html'
    context = {'all_posts': all_posts, 'page': page}
    return render(request, template, context)


def post(request, slug):
    single_post = get_object_or_404(Post.objects.all(), slug=slug)
    template = 'post.html'
    context = {'post': single_post}
    return render(request, template, context)
