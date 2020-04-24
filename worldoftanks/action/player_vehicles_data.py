import os
from datetime import datetime
from sqlalchemy.orm import sessionmaker

from worldoftanks.helper.logger import create_logger
from worldoftanks.helper.create_engine import create_db_engine
from worldoftanks.utils.api import API
from worldoftanks.orm.data_model import PlayerPersonalVehiclesModel


class PlayerVehiclesData:

    def __init__(self, log_level: str):
        self.logger = create_logger(log_level)

    def _extract_data(self, application_id: str, account_id: str, token: str) -> dict:
        """
        Extracts Data from the api
        """

        self.logger.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, token=token)
        raw_data = wot.get_data(source='player_vehicles_data')

        return raw_data

    def _parse_data(self, raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        self.logger.info('Parsing player personal details data')

        # Get only the account data
        account_data = raw_data['data'][account_id]

        clean_data = []
        for item in account_data:
            clean_data.append({
                "tank_id": item['tank_id'],
                "battles": item['statistics']['battles'],
                "mark_of_mastery": item['mark_of_mastery'],
                "wins": item['statistics']['wins']
            })

        return clean_data

    def _load_data(self, data: list):
        """
        Loads the data into the database using the ORM.
        """

        try:
            Session = sessionmaker(bind=create_db_engine(path=os.getcwd()))
            session = Session()
            session.bulk_insert_mappings(PlayerPersonalVehiclesModel, data)
            session.commit()
            session.close()
            self.logger.info('Player vehicles data Loaded into database')

        except:
            # TODO: Create a less generic exception
            self.logger.error('Player vehicles data loading data failed')
            raise

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            self._load_data(data=clean_data)

        return clean_data
