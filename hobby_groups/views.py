from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from hobby_groups.forms import CreateHobbyGroupForm, EditHobbyGroupForm
from hobby_groups.mixins import GroupAdminRequiredMixin
from hobby_groups.models import HobbyGroup, GroupMembership
from posts.forms import CreatePostForm


class CreateHobbyGroupView(LoginRequiredMixin, CreateView):
    model = HobbyGroup
    form_class = CreateHobbyGroupForm
    template_name = 'hobbygroups/create-group.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('register')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)

        GroupMembership.objects.create(
            user=self.request.user,
            group=self.object,
            is_admin=True
        )

        return response

class HobbyGroupDetailView(FormMixin, DetailView):
    model = HobbyGroup
    template_name = 'hobbygroups/group-details.html'
    context_object_name = 'group'
    form_class = CreatePostForm

    def get_success_url(self):
        return reverse('group-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['posts'] = self.object.posts.all().order_by('-created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form_class()(self.request.POST)

        user = request.user

        if not user.is_authenticated:
            messages.error(request, "You must be logged in and a group member to post.")
            return redirect(self.request.path_info)


        if not GroupMembership.objects.filter(user=user, group=self.object).exists():
            messages.error(request, "Only group members can make posts.")
            return redirect(self.request.path_info)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.group = self.object
            post.save()
            return redirect(self.get_success_url())
        else:
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

class JoinGroupView(LoginRequiredMixin, View):
    login_url = reverse_lazy('register')

    @staticmethod
    def post(request, pk):
        group = get_object_or_404(HobbyGroup, pk=pk)

        if not GroupMembership.objects.filter(user=request.user, group=group).exists():
            GroupMembership.objects.create(user=request.user, group=group)

        return redirect('group-details', pk=pk)

class LeaveGroupView(View):

    @staticmethod
    def post(request, pk):
        group = get_object_or_404(HobbyGroup, pk=pk)
        membership = GroupMembership.objects.get(user=request.user, group=group)

        if membership.is_admin and group.groupmembership_set.filter(is_admin=True).count() == 1:
            messages.error(request, "You are the only admin. You can't leave the group.")
            return redirect('group-details', pk=pk)

        membership.delete()
        return redirect('home')

class EditHobbyGroupView(GroupAdminRequiredMixin, UpdateView):
    model = HobbyGroup
    form_class = EditHobbyGroupForm
    template_name = 'hobbygroups/edit-group.html'

    def get_success_url(self):
        return reverse('group-details', kwargs={'pk': self.object.pk})

class DeleteHobbyGroupView(GroupAdminRequiredMixin, DeleteView):
    model = HobbyGroup
    template_name = 'hobbygroups/delete-group.html'
    success_url = reverse_lazy('home')
