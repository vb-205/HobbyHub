from django.urls import path
from django.contrib.auth.views import LoginView
from accounts.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]