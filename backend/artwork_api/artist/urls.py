from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import UserRegisterView,ChangePasswordsView,UpdateProfileView,ShowProfileView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name="register"),
    path('edit_profile/',UpdateProfileView.as_view(),name='edit_profile'),
    path('password/', ChangePasswordsView.as_view(),name='changePassword'),
    path('profile/<int:pk>', ShowProfileView.as_view(),name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)