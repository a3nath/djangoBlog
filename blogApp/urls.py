from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting-page"),
    path("posts/", views.posts.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.post_det.as_view(), name="post-detail-page")
]
