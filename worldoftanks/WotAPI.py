import os

from worldoftanks.helper.validators import Validators
from worldoftanks.helper.create_engine import create_db_engine
from worldoftanks.helper.logger import create_logger
from worldoftanks.orm.data_model import DataModel
from worldoftanks.action.player_personal_data import PlayerPersonalData
from worldoftanks.action.player_vehicles_data import PlayerVehiclesData
from worldoftanks.action.player_achievements import PlayerAchievementsData
from worldoftanks.action.tankopedia_vehicles import TankopediaVehiclesData
from worldoftanks.action.tankopedia_achievements import TankopediaAchievementsData
from worldoftanks.action.tankopedia_info import TankopediaInfoData
from worldoftanks.action.tankopedia_maps import TankopediaMapsData


class WotAPI:

    def __init__(self, application_id: str, account_id: str, token: str, realm:str, quietly=False, log_level="WARNING"):
        self.log_level = create_logger(log_level)
        self.quietly = quietly
        self.application_id = application_id
        self.account_id = account_id
        self.token = token
        self.realm = realm

    def _check_parameters(self):
        """
        Validates if the application id, account_id and token exist.
        """
        Validators.check_if_param_exists(self.token, 'token')
        Validators.check_if_param_exists(self.account_id, 'account_id')
        Validators.check_if_param_exists(self.application_id, 'application_id')

    def db_init(self):
        """
        Creates the sqlite database and all tables for data to be populated.
        """
        engine = create_db_engine(path=os.getcwd())
        DataModel.create_tables(engine=engine)
        if not self.quietly:
            print('Database created')

    def player_personal(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of personal data into the database.
        Requires a personal access token.
        """

        self._check_parameters()

        personal_data = PlayerPersonalData()
        data = personal_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db)

        if not self.quietly:
            print('Player personal data has been extracted')

        return data

    def player_vehicles(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player vehicle data into the database.
        Requires a personal access token.
        """
        self._check_parameters()

        vehicles_data = PlayerVehiclesData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db)

        if not self.quietly:
            print("Player personal vehicles data has been extracted")
        return data

    def player_achievements(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player achievements data into the database.
        Requires a personal access token.
        """
        self._check_parameters()

        vehicles_data = PlayerAchievementsData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db)

        if not self.quietly:
            print("Player personal achievements data has been extracted")
        return data

    def tankopedia_vehicles(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia vehicles data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaVehiclesData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, load_once=load_once)

        if not self.quietly:
            print("Player tankopedia vehicles data has been extracted")
        return data

    def tankopedia_achievements(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia achievements data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaAchievementsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                 load_to_db=load_to_db, load_once=load_once)

        if not self.quietly:
            print("Player tankopedia achievements has been extracted")
        return data

    def tankopedia_information(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia information data into the database.
        """
        self._check_parameters()

        info = TankopediaInfoData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                             load_to_db=load_to_db, load_once=load_once)

        if not self.quietly:
            print("Player tankopedia information has been extracted")
        return data

    def tankopedia_maps(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia maps data into the database.
        """
        self._check_parameters()

        info = TankopediaMapsData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                             load_to_db=load_to_db, load_once=load_once)

        if not self.quietly:
            print("Player tankopedia maps has been extracted")
        return data

