from http import HTTPStatus

from django.test import TestCase
from smallurl.shortener.models import Shortener


class ShortenerFormTests(TestCase):
    def setUp(self):
        self.target_url = "https://github.com/"
        self.shortener = Shortener.objects.create(full_url=self.target_url)

    def test_rediction_url(self):
        response = self.client.get(f"/{self.shortener.hash_url}", allow_redirects=False)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_redirection_location(self):
        response = self.client.get(f"/{self.shortener.hash_url}", allow_redirects=False)

        self.assertEqual(response.headers['Location'], self.target_url)