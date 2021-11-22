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
from worldoftanks.action.tankopedia_badges import TankopediaBadgesData
from worldoftanks.action.vehicles_statistics import VehicleStatisticsData
from worldoftanks.action.vehicles_achievements import VehicleAchievementsData


class WotAPI:

    def __init__(self, application_id: str, account_id: str, realm: str, quietly=False,
                 logging_enabled=False, log_level="WARNING", load_to_db=True, db_path=os.getcwd()):
        if logging_enabled:
            self.log_level = create_logger(log_level)
        self.quietly = quietly
        self.application_id = application_id
        self.account_id = account_id
        self.realm = realm
        self.load_to_db = load_to_db
        self.db_path = db_path

        if self.load_to_db:
            """
            Create the database at the declared path. 
            """
            engine = create_db_engine(path=self.db_path)
            DataModel.create_tables(engine=engine)
            if not self.quietly:
                print('Database created')

    def _check_parameters(self):
        """
        Validates if the application id, account_id and  exist.
        """
        Validators.check_if_param_exists(self.account_id, 'account_id')
        Validators.check_if_param_exists(self.application_id, 'application_id')
        Validators.check_realm(self.realm)

    def player_personal(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of personal data into the database.
        Requires a personal access .
        """

        self._check_parameters()

        personal_data = PlayerPersonalData()
        data = personal_data.etl_data(application_id=self.application_id, account_id=self.account_id,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print('Player personal data has been extracted')

        return data

    def player_vehicles(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player vehicle data into the database.
        Requires a personal access .
        """
        self._check_parameters()

        vehicles_data = PlayerVehiclesData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Player personal vehicles data has been extracted")
        return data

    def player_achievements(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of player achievements data into the database.
        Requires a personal access .
        """
        self._check_parameters()

        vehicles_data = PlayerAchievementsData()
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id,
                                      load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Player personal achievements data has been extracted")
        return data

    def tankopedia_vehicles(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia vehicles data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaVehiclesData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id,
                                 load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia vehicles data has been extracted")
        return data

    def tankopedia_achievements(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia achievements data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaAchievementsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id,
                                 load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia achievements has been extracted")
        return data

    def tankopedia_information(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia information data into the database.
        """
        self._check_parameters()

        info = TankopediaInfoData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id,
                             load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia information has been extracted")
        return data

    def tankopedia_maps(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of tankopedia maps data into the database.
        """
        self._check_parameters()

        info = TankopediaMapsData()
        data = info.etl_data(application_id=self.application_id, account_id=self.account_id,
                             load_to_db=load_to_db, load_once=load_once, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia maps has been extracted")
        return data

    def tankopedia_badges(self, load_once: bool, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = TankopediaBadgesData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id,
                                 load_to_db=load_to_db, realm=self.realm, load_once=load_once, db_path=self.db_path)

        if not self.quietly:
            print("Tankopedia badges have been extracted")
        return data

    def vehicle_statistics(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = VehicleStatisticsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id,
                                 load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Vehicle statistics has been extracted")
        return data

    def vehicle_achievements(self, load_to_db=True) -> list:
        """
        Handles the extraction, transformation and loading of vehicle statistics data into the database.
        """
        self._check_parameters()

        vehicles = VehicleAchievementsData()
        data = vehicles.etl_data(application_id=self.application_id, account_id=self.account_id,
                                 load_to_db=load_to_db, realm=self.realm, db_path=self.db_path)

        if not self.quietly:
            print("Vehicle achievements has been extracted")
        return data

