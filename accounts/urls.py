from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, ProfileDetailView, ProfileEditView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/<int:pk>/', include([
        path('profile-details/', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='edit-profile'),
    ]))
]