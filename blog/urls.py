from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog,name="home-page"),
    path("posts",views.posts,name="post-page"),
    path("posts/<slug:slug>",views.posts_details,name="detail-page")

]
