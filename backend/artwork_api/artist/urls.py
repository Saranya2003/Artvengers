from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import create_profile_action, UserRegisterView,ChangePasswordsView,UpdateProfileView,ShowProfileView,updateprofile,CreateProfileView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/<int:pk>',UpdateProfileView.as_view(),name='edit_profile'),
    path('edit_profile/<int:pkreq>/updateaction',updateprofile,name='edit_profile_action'),
    path('password/', ChangePasswordsView.as_view(),name='changePassword'),
    path('profile/<int:pk>', ShowProfileView.as_view(),name='profile'),
    path('profile/', CreateProfileView.as_view(),name='create_profile'),
    path('createprofileaction/', create_profile_action,name='create_profile_action'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)