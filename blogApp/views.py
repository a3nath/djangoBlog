from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag, Comment
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse


##list view
class StartingPageView(ListView):
    template_name = "blogApp/index.html"
    queryset = Post.objects.order_by("-date")[:2]
    ##name to refer the output in the template
    context_object_name = "posts"


# for our post url
#list view
class AllPostView(ListView):
    template_name = "blogApp/posts.html"
    queryset = Post.objects.order_by("-date")
    context_object_name = "all_posts"


#for an individual post
#detail view

class PostDetailView(View):
    
    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        post_tags = post.tag.all()
        comment_form = CommentForm()
        comments = post.comments.all()
        context = {
            "post": post,
            "post_tags" : post_tags,
            "comment_form": comment_form, 
            "comments": comments
        }
        return render(request, "blogApp/post-detail.html",context)

    def post(self, request, slug):
        post = Post.objects.get(slug = slug)
        post_tags = post.tag.all()
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid:
            ##allows to save user input
            comment = comment_form.save(commit=False)
            ##add extra data
            comment.post = post
            ##save to db
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags" : post_tags,
            "comment_form": comment_form,
            "comments" : post.comments.all()
            }
        return render(request, "blogApp/post-detail.html", context)


