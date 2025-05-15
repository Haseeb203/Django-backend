from django.shortcuts import render ,get_object_or_404
from .models import Post

# Create your views here.

posts = [
   
]



def starting_page(request):
    latest_post=Post.objects.all().order_by("-date")[:3]
    return render(request , "blog/index.html" ,{
        "posts":latest_post
    })


def all_posts(request):
    posts=Post.objects.all().order_by("-date")
    return render(request , "blog/all-posts.html" , {
        "posts":posts
    })


def single_post(request , slug):
    identified_post=get_object_or_404(Post , slug=slug)
    return render(request , "blog/single-post.html" ,{
        "post": identified_post ,
        "post_tags": identified_post.tags.all()
    })