import logging

from worldoftanks.helper.data_model_loader import DataModelLoader
from worldoftanks.utils.api import API
from worldoftanks.orm.data_model import TankopediaInfoModel


class TankopediaInfoData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player vehicles data')

        wot = API(application_id=application_id, account_id=account_id, token=token, realm=realm)
        raw_data = wot.get_data(source='tankopedia_info')

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing tankopedia info details data')

        # Get only the account data
        info_data = raw_data['data']

        clean_data = []

        for metric in ['vehicle_crew_roles', 'languages', 'vehicle_types', 'vehicle_nations']:
            for key, value in info_data[metric].items():
                clean_data.append({
                    "metric": metric,
                    "group": None,
                    "alias": key,
                    "value": value
                })

        # Get the achievement sections
        for key, value in info_data['achievement_sections'].items():
            clean_data.append({
                "metric": "achievement_sections",
                "group": key,
                "alias": value['name'],
                "value": value['order']
            })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool, load_once: bool,
                 realm: str) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token, realm=realm)
        clean_data = self._parse_data(raw_data=raw_data)

        if load_to_db:
            if load_once:
                # Checks if the data is already existing in the database else loads it.
                if DataModelLoader.check_if_data_exists(TankopediaInfoModel):
                    logging.info('Tankopedia information data will not be loaded into the database.')
                else:
                    DataModelLoader.insert(TankopediaInfoModel, clean_data)
            else:
                DataModelLoader.insert(TankopediaInfoModel, clean_data)

        return clean_data
