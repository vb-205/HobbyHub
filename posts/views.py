from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DeleteView, DetailView
from django.views.generic.edit import FormMixin
from posts.forms import CreateCommentForm
from posts.models import Post

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post-details.html'
    context_object_name = 'post'
    form_class = CreateCommentForm

    def get_success_url(self):
        return reverse('post-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
            return redirect('register')

        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)
class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return HttpResponseForbidden("You are not allowed to delete this post.")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('group-details', kwargs={'pk': self.object.group.pk})

