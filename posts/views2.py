from .models import post
from django.views import generic


class Postlist(generic.ListView):
    model = post
    # return context =  post_list , object_list  (name_operation)
    # return templates = post_list.html


class postDetail(generic.DeleteView):
    model = post
    # context = post


class addpost(generic.CreateView):
    model = post
    fields = ['author', 'title', 'content', 'tags', 'image']
    success_url = '/blog/'


class Editpost(generic.UpdateView):
    model = post
    fields = ['author', 'title', 'content', 'tags', 'image']
    success_url = '/blog/'
    template_name = 'posts/edit.html'


class DeletePost(generic.DeleteView):
    model = post
    success_url = '/blog/'

