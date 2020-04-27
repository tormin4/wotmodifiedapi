import unittest

from worldoftanks.utils.api import API
# Note: Private methods shouldn't really be tested but this is vital to the building of correct endpoints


class TestAPI(unittest.TestCase):
    api = API(application_id='1234', account_id='1234', token='1234', realm='eu')

    def test_api_application_id(self):
        self.assertEqual(self.api.BASE_URL, "https://api.worldoftanks.eu/wot")

    def test_get_data_non_existent_source(self):
        self.assertRaises(ValueError, self.api.get_data, 'some_garbage')

    def test_api_response_codes(self):
        self.assertRaises(ConnectionError, self.api.get_data, 'player_personal_data')

    def test_url_build_vehicle_statistics(self):
        url = self.api._build_url_vehicle_statistics()
        expected = 'https://api.worldoftanks.eu/wot/tanks/stats/?application_id=1234&access_token=1234&account_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_vehicle_achievements(self):
        url = self.api._build_url_vehicle_achievements()
        expected = 'https://api.worldoftanks.eu/wot/tanks/achievements/?application_id=1234&access_token=1234&account_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_player_personal(self):
        url = self.api._build_url_player_personal()
        expected = 'https://api.worldoftanks.eu/wot/account/info/?application_id=1234&access_token=1234&account_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_player_vehicles(self):
        url = self.api._build_url_player_vehicles()
        expected = 'https://api.worldoftanks.eu/wot/account/tanks/?application_id=1234&access_token=1234&account_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_player_achievements(self):
        url = self.api._build_url_player_achievements()
        expected = 'https://api.worldoftanks.eu/wot/account/achievements/?application_id=1234&account_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_tankopedia_vehicles(self):
        url = self.api._build_url_tankopedia_vehicles()
        expected = 'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/?application_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_tankopedia_achievements(self):
        url = self.api._build_url_tankopedia_achievements()
        expected = 'https://api.worldoftanks.eu/wot/encyclopedia/achievements/?application_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_tankopedia_information(self):
        url = self.api._build_url_tankopedia_information()
        expected = 'https://api.worldoftanks.eu/wot/encyclopedia/info/?application_id=1234'
        self.assertEqual(url, expected)

    def test_url_build_tankopedia_maps(self):
        url = self.api._build_url_tankopedia_maps()
        expected = 'https://api.worldoftanks.eu/wot/encyclopedia/arenas/?application_id=1234'
        self.assertEqual(url, expected)