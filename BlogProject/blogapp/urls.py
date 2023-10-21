from django.urls import path
from blogapp import views


urlpatterns = [
     path("",views.starting_page,name='starting-page'),
     path("posts",views.posts,name="posts-page"),
     path("all_posts/<slug:slug>",views.post_details,name='posts-details-page'),
     #posts/my-first-post
]

