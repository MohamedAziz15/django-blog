from django.shortcuts import render, redirect
from .models import post
from .forms import postform
# Create your views here.


def post_list(request):
    data = post.objects.all()  # orm ->> sql ->> db ->> return list(all posts)
    return render(request, 'posts.html', {'posts': data})


def post_details(request, post_id):
    # orm ->> sql ->> db ->> return list(all posts)
    data = post.objects.get(id=post_id)
    return render(request, 'post_details.html', {'post': data})


def add_post(request):

    if request.method == 'POST':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog/')

    else:
        form = postform()
    return render(request, 'new.html', {'form': form})
