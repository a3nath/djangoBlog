from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView


##list view
class starting_page(ListView):
    template_name = "blogApp/index.html"
    queryset = Post.objects.order_by("-date")[:2]
    ##name to refer the output in the template
    context_object_name = "posts"

    # def get_query_set(self):
    #     base_query = super().get_queryset()
    #     data = base_query.order_by("-date")[:1]
    #     return data


# def starting_page(request):
#     all_posts = Post.objects.all().order_by("-date")
#     latestPost = all_posts[:2]
#     return render(request, "blogApp/index.html", {'posts':latestPost})

# for our post url
#list view
class posts(ListView):
    template_name = "blogApp/posts.html"
    queryset = Post.objects.order_by("-date")
    context_object_name = "posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blogApp/posts.html", {'posts': all_posts})

#for an individual post
#detail view

class post_det(DetailView):
    template_name = 'blogApp/post-detail.html'
    # queryset = Post.objects.filter(slug=slug)
    model = Post
    context_object_name = 'post'

# def post_det(request, slug):
#     selectedPost = get_object_or_404(Post, slug=slug)
#     return render(request, "blogApp/post-detail.html", 
#         {'post':selectedPost,
#         'post_tags': selectedPost.tag.all()})