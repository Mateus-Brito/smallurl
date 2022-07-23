from http import HTTPStatus

from django.test import TestCase
from smallurl.shortener.models import Shortener


class ShortenerFormTests(TestCase):
    def setUp(self):
        self.shortener = Shortener.objects.create(full_url="https://github.com/")

    def test_valid_hash_url(self):
        self.assertIsNotNone(self.shortener.hash_url)

    def test_follow_url(self):
        self.shortener.follow()
        self.assertEqual(self.shortener.times_followed, 1)
        
