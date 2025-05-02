import unittest
from unittest.mock import patch

from src.api_client import get_location


class ApiClientTest(unittest.TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "ipAddress": "8.8.8.8",
            "countryName": "United States of America",
            "cityName": "Mountain View",
            "regionName": "California",
            "latitude": 37.386051,
            "longitude": -122.083847,
            "timeZone": "-07:00",
        }

        response = get_location("8.8.8.8")
        self.assertEqual(response["country"], "United States of America")
        self.assertEqual(response["city"], "Mountain View")
        self.assertEqual(response["region"], "California")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
