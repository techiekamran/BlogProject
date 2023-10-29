from django.shortcuts import render, get_object_or_404
from datetime import date
from blogapp.models import Author, Post, Tag
# Create your views here.


data = [
    {
        "slug": "hikeinthemountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
        """
    }
]

def get_date(data):
    return data['date']



def home(request):
    #sorted_post = sorted(data,key=get_date)
    #latest_post = sorted_post[-2:]
    latest_post = Post.objects.all().order_by('-Date')[:2]
    return render(request,'blogapp/home.html',{'all_posts':latest_post})

def posts(request):
    posts_data = Post.objects.all()
    return render(request,'blogapp/all-post.html',{'all_posts':posts_data})
    #return render(request,'blogapp/all-post.html',{'all_posts':data})


def post_details(request,slug):
    single_post = get_object_or_404(Post,slug=slug)
    #single_post = Post.objects.get(slug=slug)
    #single_post= next(post for post in data if post['slug']==slug)
    return render(request,'blogapp/post-detail.html',{'post':single_post,
                                                      'post_tags':single_post.tag.all()})

