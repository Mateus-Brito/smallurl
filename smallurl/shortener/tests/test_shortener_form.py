from http import HTTPStatus

from django.test import TestCase


class ShortenerFormTests(TestCase):
    def test_post_success(self):
        response = self.client.post("/", data={"full_url": "https://github.com"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "https://github.com")

    def test_post_empty(self):
        response = self.client.post("/", data={"full_url": ""})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "The link url field is required.")

    def test_post_invalid_url(self):
        response = self.client.post("/", data={"full_url": "teste"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Enter a valid URL.")
