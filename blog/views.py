from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
    context = {
        #'blogs': Blog.objects.order_by('-date')[:5],
        'blogs': Blog.objects.order_by('-date'),
    }
    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)
