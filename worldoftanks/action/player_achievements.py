import logging

from worldoftanks.helper.data_model_loader import DataModelLoader
from worldoftanks.utils.api import API
from worldoftanks.orm.data_model import PlayerAchievementsModel


class PlayerAchievementsData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, token: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player achivements data')

        wot = API(application_id=application_id, account_id=account_id, token=token)
        raw_data = wot.get_data(source='player_achievements')

        return raw_data

    @staticmethod
    def _parse_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player achievements data')

        # Get only the account data
        account_data = raw_data['data'][account_id]

        clean_data = []
        for medal_type in ['achievements', 'frags', 'max_series']:
            for key, value in account_data[medal_type].items():
                clean_data.append({
                    "medal_type": medal_type,
                    "medal_name": key,
                    "medal_quantity": value
                })

        return clean_data

    def etl_data(self, application_id: str, account_id: str, token: str, load_to_db: bool) -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, token=token)
        clean_data = self._parse_data(raw_data=raw_data, account_id=account_id)

        if load_to_db:
            DataModelLoader.insert(PlayerAchievementsModel, clean_data)

        return clean_data
