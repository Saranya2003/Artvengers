from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', views.ListArtwork.as_view(),name="artwork_list"),
    path('list/<int:pk>/', views.DetailArtwork.as_view(),name="artwork_detail"),
    path('albumlist/', views.ListAlbum.as_view(),name="album_list"),
    path('', views.home, name="home"),
    path('artwork/addcollection/<int:pk>', views.addtoalbum,name="add_to_album_action"),
    path('artwork/<int:pk>', views.ArtworkPostDetail.as_view(), name="artwork_detail"),
    path('artwork/edit/<int:pk>', views.UpdateArtworks.as_view(), name="artwork_edit"),
    path('artwork/edit/<int:pkreq>/update', views.updateartworkpost, name="artwork_edit_action"),
    path('explore/', views.ExploreView.as_view(), name="explore"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('add_artwork/', views.AddArtwork.as_view(), name="add_artwork"),
    path('add_album/', views.AddAlbum.as_view(), name="add_album"),
    path('album/edit/<int:pk>', views.UpdateAlbum.as_view(), name="album_edit"),
    path('album/edit/<int:pkreq>/update', views.updatealbum, name="update_album_action"),
    path('search_result/',views.SearchView.as_view(),name="search_result"),
    path('tag/<str:Tag>',views.TagsView.as_view(),name="tag"),
    path('album/<int:pk>',views.AlbumView.as_view(),name="album"),
    path('upload/',views.uploadPage, name="upload"),
    path('artwork/<int:pk>/delete',views.DeleteArtwork.as_view(), name="delete_artwork"),
    path('album/<int:pk>/delete',views.DeleteAlbum.as_view(), name="delete_album"),
    path('tags/',views.Taglist.as_view(),name="Tags"),
    path('search_mobile/',views.SearchMobileView.as_view(),name="search_mobile"),
    path('artwork/<int:pk>/like/',views.LikeView,name="like_artwork"),
    path('artwork/<int:pk>/comment/',views.post_comment,name="add_comment"),
    path('artwork/upload/', views.insertartwork,name="add_artwork_action"),
    path('album/upload/', views.insertalbum,name="add_album_action"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)