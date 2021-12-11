from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag
from django.views.generic import ListView

#dummy data


# fcn to get date

#  views


##list view
class starting_page(ListView):
    template_name = "blogApp/index.html"
    queryset = Post.objects.order_by("-date")[:2]
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
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blogApp/posts.html", {'posts': all_posts})

#for an individual post
#detail view
def post_det(request, slug):
    selectedPost = get_object_or_404(Post, slug=slug)
    return render(request, "blogApp/post-detail.html", 
        {'post':selectedPost,
        'post_tags': selectedPost.tag.all()})



