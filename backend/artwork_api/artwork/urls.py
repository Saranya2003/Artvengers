from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.ListArtwork.as_view()),
    path('list/<int:pk>/', views.DetailArtwork.as_view()),
    path('', views.home, name="home"),
    path('post/<int:pk>', views.Artwork_Post_Detail.as_view(), name="post_detail"),
    path('post/', views.Artwork_Post_List.as_view(), name="post_list"),
    path('explore/', views.explore, name="explore"),
    path('dashboard/', views.dashboard, name="dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)