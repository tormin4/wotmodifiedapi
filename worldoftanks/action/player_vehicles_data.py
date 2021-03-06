import logging

from worldoftanks.helper.data_model_loader import DataModelLoader
from worldoftanks.utils.api import API
from worldoftanks.orm.data_model import PlayerPersonalVehiclesModel


class PlayerVehiclesData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, realm=realm)
        raw_data = wot.get_data(source='player_vehicles_data')

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player vehicles details data')

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

    def etl_data(self, application_id: str, account_id: str, load_to_db: bool, realm: str, db_path: str) \
            -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            DataModelLoader.insert(PlayerPersonalVehiclesModel, clean_data, db_path=db_path)

        return clean_data
