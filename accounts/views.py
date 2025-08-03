from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import AppUserCreationForm, ProfileEditForm
from accounts.models import Profile
from hobby_groups.models import HobbyGroup

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response

class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        joined_groups = HobbyGroup.objects.filter(groupmembership__user=user)

        context['joined_groups'] = joined_groups
        return context

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'edit-profile.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        return reverse(
            'profile-details',
            kwargs={'pk': self.object.user.pk}
        )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

