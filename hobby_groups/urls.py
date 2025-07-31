from django.urls import path, include
from hobby_groups import views

urlpatterns = [
    path('create-group/', views.CreateHobbyGroupView.as_view(), name='create-group'),
    path('<int:pk>/', include([
        path('details/', views.HobbyGroupDetailView.as_view(), name='group-details'),
        path('join/', views.JoinGroupView.as_view(), name='join-group'),
        path('leave/', views.LeaveGroupView.as_view(), name='leave-group'),
        path('edit/', views.EditHobbyGroupView.as_view(), name='edit-group'),
        path('delete/', views.DeleteHobbyGroupView.as_view(), name='delete-group'),
    ]))
]