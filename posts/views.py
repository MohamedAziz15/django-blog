from django.shortcuts import render
from .models import post
# Create your views here.


def post_list(request):
    data = post.objects.all()  # orm ->> sql ->> db ->> return list(all posts)
    return render(request,'posts.html',{'posts':data})
