
from django.shortcuts import render
import blog
from django.http import Http404,HttpResponse,HttpResponseNotFound,HttpResponseRedirect

from .models import Post

# Create your views here.

def blog(request):
        latest_posts=Post.objects.all().order_by("-date")[:3]  #order in decending order
        return render(request,"blog/home.html",{
            "all_posts":latest_posts,
        })
    

def posts(request):
    all_posts=Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html",{
        "all_post":all_posts,
    }) 

def posts_details(request,slug):
    try:
        identified_post= Post.objects.get(slug=slug)
    except:
        return Http404();
    return render(request,"blog/post_detail.html" ,{
        "post":identified_post,
    })

