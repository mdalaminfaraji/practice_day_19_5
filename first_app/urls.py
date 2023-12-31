# your_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, HomeView ,  MusicianListView,MusicianCreateView,MusicianUpdateView,AlbumCreateView,AlbumUpdateView,AlbumDeleteView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'), 
    path('musician-list/', MusicianListView.as_view(), name='musician-list'),
    path('musician-create/', MusicianCreateView.as_view(), name='musician-create'),
    path('musician-update/<int:pk>/', MusicianUpdateView.as_view(), name='musician-update'),
    path('album-create/', AlbumCreateView.as_view(), name='album-create'),
    path('album-update/<int:pk>/', AlbumUpdateView.as_view(), name='album-update'),
    path('album-delete/<int:pk>/', AlbumDeleteView.as_view(), name='album-delete'),
]
