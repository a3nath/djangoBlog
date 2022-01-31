from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView


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

class PostDetalView(DetailView):

    #if get request display form
    #if post request new view
    template_name = 'blogApp/post-detail.html'
    model = Post
    context_object_name = 'post'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tag.all()
        context['comment_form'] = CommentForm()
        return context
    

# def post_det(request, slug):
#     selectedPost = get_object_or_404(Post, slug=slug)
#     return render(request, "blogApp/post-detail.html", 
#         {'post':selectedPost,
#         'post_tags': selectedPost.tag.all()})