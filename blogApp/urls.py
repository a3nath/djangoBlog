from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_det, name="post-detail-page")
]
