from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.ListArtwork.as_view()),
    path('list/<int:pk>/', views.DetailArtwork.as_view()),
    path('', views.home, name="home"),
    path('artwork/<int:pk>', views.Artwork_Post_Detail.as_view(), name="artwork_detail"),
    path('artwork/edit', views.UpdateArtworks.as_view(), name="artwork_edit"),
    path('artwork/', views.Artwork_Post_List.as_view(), name="artwork_list"),
    path('explore/', views.explore, name="explore"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_artwork/', views.AddArtwork.as_view(), name="add_artwork"),
    path('add_album/', views.AddAlbum.as_view(), name="add_album"),
    path('album/edit', views.UpdateAlbum.as_view(), name="album_edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)