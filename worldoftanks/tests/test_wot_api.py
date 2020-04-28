import unittest
import os

from worldoftanks.WotAPI import WotAPI


class TestWotAPI(unittest.TestCase):
    wot = WotAPI(application_id='1234',
                 account_id='1234',
                 token='12er',
                 realm='eu',
                 quietly=True)

    def test_database_initialization(self):
        os.remove('world_of_tanks.db')

    def test_check_validators(self):
        self.wot._check_parameters()

    def test_player_personal_fail(self):
        self.assertRaises(ConnectionError, self.wot.player_personal)

    def test_player_vehicles_fail(self):
        self.assertRaises(ConnectionError, self.wot.player_vehicles)

    def test_player_achievements_fail(self):
        self.assertRaises(ConnectionError, self.wot.player_achievements)

    def test_tankopedia_vehicles_fail(self):
        self.assertRaises(ConnectionError, self.wot.tankopedia_vehicles, False)

    def test_tankopedia_achievements_fail(self):
        self.assertRaises(ConnectionError, self.wot.tankopedia_achievements, False)

    def test_tankopedia_information_fail(self):
        self.assertRaises(ConnectionError, self.wot.tankopedia_information, False)

    def test_tankopedia_maps_fail(self):
        self.assertRaises(ConnectionError, self.wot.tankopedia_maps, False)

    def test_tankopedia_badges_fail(self):
        self.assertRaises(ConnectionError, self.wot.tankopedia_badges, False)

    def test_vehicle_statistics_fail(self):
        self.assertRaises(ConnectionError, self.wot.vehicle_statistics)

    def test_vehicle_achievements_fail(self):
        self.assertRaises(ConnectionError, self.wot.vehicle_achievements)
