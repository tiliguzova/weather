from django.test import TestCase, Client
from unittest.mock import patch
from django.urls import reverse
from app.models import *
from app.forms import *


class WeatherTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CityForm)
        self.assertEqual(response.context['weather'], "")
        self.assertEqual(response.context['error'], "")

    @patch('app.views.requests.get')
    def test_post_true(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "main": {"temp": 20, "humidity": 60, "pressure": 1012},
            "weather": [{"description": "ясно"}],
            "wind": {"speed": 5}
        }
        response = self.client.post(self.url, {"city": "Москва"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CityForm)
        self.assertIsInstance(response.context['weather'], Weather)
        self.assertEqual(response.context['error'], "")

    @patch('app.views.requests.get')
    def test_post_false(self, mock_get):
        mock_get.return_value.status_code = 404
        response = self.client.post(self.url, {"city": "Aboba"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], CityForm)
        self.assertEqual(response.context['weather'], "")
        self.assertEqual(response.context['error'], "Город не найден")
