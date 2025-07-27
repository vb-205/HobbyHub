from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import AppUserCreationForm, ProfileEditForm


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

