from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.ListArtwork.as_view(),name="artwork_list"),
    path('list/<int:pk>/', views.DetailArtwork.as_view(),name="artwork_detail"),
    path('albumlist/', views.ListAlbum.as_view(),name="album_list"),
    path('', views.home, name="home"),
    path('artwork/<int:pk>', views.ArtworkPostDetail.as_view(), name="artwork_detail"),
    path('artwork/edit/<int:pk>', views.UpdateArtworks.as_view(), name="artwork_edit"),
    path('explore/', views.ExploreView.as_view(), name="explore"),
    #path('explore/', views.explore, name="explore"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('add_artwork/', views.AddArtwork.as_view(), name="add_artwork"),
    path('add_album/', views.AddAlbum.as_view(), name="add_album"),
    path('album/edit/<int:pk>', views.UpdateAlbum.as_view(), name="album_edit"),
    path('search_result/',views.SearchView,name="search_result"),
    path('tag/<str:Tag>',views.TagsView.as_view(),name="tag"),
    path('album/<int:pk>',views.AlbumView.as_view(),name="album")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)