from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, resolve_url
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    #queryset = Post.objects.filter(title_startswith='t')
    paginate_by = 10

    def get_queryset(self):
        return Post.timeline(self.request.user)

index = login_required(PostListView.as_view())

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_object(self, *args, **kwargs):
        if 'uuid' in self.kwargs:
            return get_object_or_404(Post, uuid=self.kwargs['uuid'])
        return super(PostDetailView, self).get_object(*args, **kwargs)

detail = PostDetailView.as_view()

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.ip = self.request.META['REMOTE_ADDR']
        return super(PostCreateView, self).form_valid(form)

    # def get_success_url(self):
    #     return reverse('blog:detail', args=[self.object.pk])

new = login_required(PostCreateView.as_view())

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'

edit = PostUpdateView.as_view()

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_new = CommentCreateView.as_view()

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'form.html'

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_edit = CommentUpdateView.as_view()

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_delete_confirm.html'

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_delete = CommentDeleteView.as_view()