from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .views import ListArtwork,DetailArtwork,DetailView,ArtworkPostDetail,ExploreView,DashboardView,AddArtwork

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, ListArtwork)
    