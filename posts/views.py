from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
    )

from django.urls import reverse_lazy
from .models import Post


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'subtitle', 'body', 'author', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
        template_name = "posts/detail.html"
        model = Post

class PostUpdateView(UpdateView):
        template_name = "posts/edit.html"
        model = Post
        fields = ['title', 'subtitle', 'body', 'status']

class PostDeleteView(DeleteView):
        template_name = "posts/delete.html"
        model = Post
        success_url = reverse_lazy('list')

class PostListView(ListView):
        template_name = "posts/list.html"
        model = Post
        

