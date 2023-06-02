from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.ListArtwork.as_view()),
    path('list/<int:pk>/', views.DetailArtwork.as_view()),
    path('albumlist/', views.ListAlbum.as_view()),
    path('', views.home, name="home"),
    path('artwork/<int:pk>', views.ArtworkPostDetail.as_view(), name="artwork_detail"),
    path('artwork/edit/<int:pk>', views.UpdateArtworks.as_view(), name="artwork_edit"),
    path("tags/<int:tag_id>",views.list_artwork_by_tag, name="tag"),
    path('explore/', views.ExploreView.as_view(), name="explore"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('add_artwork/', views.AddArtwork.as_view(), name="add_artwork"),
    path('add_album/', views.AddAlbum.as_view(), name="add_album"),
    path('album/edit/<int:pk>', views.UpdateAlbum.as_view(), name="album_edit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)