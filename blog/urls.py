from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page , name = "starting-page" ),
    path("posts" , views.posts , name = "all-posts") , 
    path("posts/<slug:slug>" , views.post_detail , name = "display-post")  #/posts/rahuls-post/  #slug concept
]