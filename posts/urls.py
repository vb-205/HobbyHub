from django.urls import path, include
from posts import views

urlpatterns = [
    path('<int:pk>/', include([
        path('details/', views.PostDetailView.as_view(), name='post-details'),
        path('delete/', views.DeletePostView.as_view(), name='delete-post'),
    ]))
]