from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Post

# Create your views here.


class PostListView(ListView):

    # specify the model for list view
    model = Post


class PostCreateView(ListView):

    # specify the model for list view
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostUpdateView(ListView):

    # specify the model for list view
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(ListView):

    # specify the model for list view
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
