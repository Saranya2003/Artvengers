from urllib import response
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from .views import ListArtwork,ListAlbum,DetailAlbum,DetailArtwork

User = get_user_model()

class ArtworkTestCase(APITestCase):
    def test_artwork(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["message"],"Artwork")

class ArtworkCreateFormTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('artwork_list')

    def authenticate(self):
        self.artist.post(reverse('register'),{
            "username":"Saranya2003",
            "email":"saranya2003@gmail.com",
            "password":"Krsk1039@#$%",
        }
        )
        self.artist.post(reverse('login'),{
            "username":"Saranya2003",
            "password":"Krsk1039@#$%",
        }
        )

        token = response.data["tokens"]["access"]

        self.artist.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_create_artwork(self):
        self.authenticate()

        sample_data = {"Title":"Sample Artwork",
                       "artist_Name":"Sample Artist",
                       "Description":"Sample Artwork",
                       "Tags":"Sample Artwork",
                       "Artwork":"Sample Artwork.jpg"}
        response = self.client.post(reverse("artwork_list"),sample_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["Title"], sample_data["Title"])

    def test_list_artwork(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])