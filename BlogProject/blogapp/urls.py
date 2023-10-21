from django.urls import path
from blogapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('all-posts',views.posts,name='all-posts'),
    path('post-details/<slug:slug>',views.post_details,name='post-details'),
]
