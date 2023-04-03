from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListArtwork.as_view()),
    path('<int:pk>/', views.DetailArtwork.as_view()),
    path('login/',views.Login.as_view()),
]