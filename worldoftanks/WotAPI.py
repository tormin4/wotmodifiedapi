import os

from worldoftanks.helper.validators import Validators
from worldoftanks.helper.create_engine import create_db_engine
from worldoftanks.orm.data_model import DataModel
from worldoftanks.action.player_personal_data import PlayerPersonalData
from worldoftanks.action.player_vehicles_data import PlayerVehiclesData


class WotAPI:

    def __init__(self, application_id: str, account_id: str, token: str, display_output=False, log_level="INFO"):
        self.log_level = log_level
        self.display_output = display_output
        self.application_id = application_id
        self.account_id = account_id
        self.token = token

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

    def player_personal_data(self, load_to_db: bool) -> list:
        """
        Handles the extraction, transformation and loading of personal data into the database.
        Requires a personal access token.
        """

        self._check_parameters()

        personal_data = PlayerPersonalData(log_level=self.log_level)
        data = personal_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db)

        return data

    def player_vehicles_data(self, load_to_db: bool) -> list:
        """
        Handles the extraction, transformation and loading of player vehicle data into the database.
        Requires a personal access token.
        """
        self._check_parameters()

        vehicles_data = PlayerVehiclesData(log_level=self.log_level)
        data = vehicles_data.etl_data(application_id=self.application_id, account_id=self.account_id, token=self.token,
                                      load_to_db=load_to_db)

        return data



