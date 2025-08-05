from django.urls import path
from common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'),
]