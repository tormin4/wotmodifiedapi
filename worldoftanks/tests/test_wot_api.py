import unittest
import os

from worldoftanks.WotAPI import WotAPI


class TestValidators(unittest.TestCase):
    wot = WotAPI(application_id='1234',
                 account_id='1234',
                 token='12er',
                 realm='eu')

    def test_database_initialization(self):

        self.wot.db_init()
        os.remove('world_of_tanks.db')

    def test_check_validators(self):
        self.wot._check_parameters()
