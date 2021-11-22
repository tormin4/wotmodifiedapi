import logging

from worldoftanks.helper.data_model_loader import DataModelLoader
from worldoftanks.utils.api import API
from worldoftanks.orm.data_model import PlayerPersonalDataStatisticsModel, PlayerPersonalDataDetailsModel


class PlayerPersonalData:

    def __init__(self):
        pass

    @staticmethod
    def _extract_data(application_id: str, account_id: str, realm: str) -> dict:
        """
        Extracts Data from the api
        """

        logging.info('Extracting player personal data')

        wot = API(application_id=application_id, account_id=account_id, realm=realm)
        raw_data = wot.get_data(source='player_personal_data')

        return raw_data

    @staticmethod
    def _parse_details_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the necessary data to be inserted into the tables
        """
        logging.info('Parsing player personal details data')
        # Get only the account data
        account_data = raw_data['data'][account_id]

        details_data = [{
            "account_id": account_id,
            "last_battle_time": account_data['last_battle_time'],
            "created_at": account_data['created_at'],
            "updated_at": account_data['updated_at'],
            "global_rating": account_data['global_rating'],
            "clan_id": account_data['clan_id']
        }]

        return details_data

    @staticmethod
    def _parse_statistics_data(raw_data: dict, account_id: str) -> list:
        """
        Extracts only the statistics data.
        The data is composed of four records based on the statistic type.
        """
        logging.info('Parsing player personal statistics data')

        raw_data = raw_data['data'][account_id]['statistics']
        statistic_types = ['clan', 'all', 'regular_team', 'company', 'stronghold_skirmish', 'stronghold_defense',
                           'historical', 'team']

        statistic_data = []
        for statistic_type in statistic_types:
            account_data = raw_data[statistic_type]
            statistic_data.append({
                "statistic_type": statistic_type,
                "spotted": account_data['spotted'],
                "battles_on_stunning_vehicles": account_data['battles_on_stunning_vehicles'],
                "avg_damage_blocked": account_data.get("avg_damage_blocked", None),
                "direct_hits_received": account_data['direct_hits_received'],
                "explosion_hits": account_data['explosion_hits'],
                "piercings_received": account_data['piercings_received'],
                "piercings": account_data['piercings'],
                "max_damage_tank_id": account_data.get("max_damage_tank_id", None),
                "xp": account_data['xp'],
                "survived_battles": account_data['survived_battles'],
                "dropped_capture_points": account_data['dropped_capture_points'],
                "hits_percents": account_data['hits_percents'],
                "draws": account_data['draws'],
                "max_xp_tank_id": account_data.get("max_xp_tank_id", None),
                "battles": account_data['battles'],
                "damage_received": account_data['damage_received'],
                "avg_damage_assisted": account_data.get("avg_damage_assisted", None),
                "max_frags_tank_id": account_data.get("max_frags_tank_id", None),
                "avg_damage_assisted_track": account_data.get("avg_damage_assisted_track", None),
                "frags": account_data['frags'],
                "stun_number": account_data['stun_number'],
                "avg_damage_assisted_radio": account_data.get("avg_damage_assisted_radio", None),
                "capture_points": account_data['capture_points'],
                "stun_assisted_damage": account_data['stun_assisted_damage'],
                "max_damage": account_data.get("max_damage", None),
                "hits": account_data['hits'],
                "battle_avg_xp": account_data['battle_avg_xp'],
                "wins": account_data['wins'],
                "losses": account_data['losses'],
                "damage_dealt": account_data['damage_dealt'],
                "no_damage_direct_hits_received": account_data['no_damage_direct_hits_received'],
                "max_frags": account_data.get("max_frags", None),
                "shots": account_data['shots'],
                "explosion_hits_received": account_data['explosion_hits_received'],
                "tanking_factor": account_data['tanking_factor']
            })

        return statistic_data

    def etl_data(self, application_id: str, account_id: str, load_to_db: bool, realm: str, db_path: str) \
            -> list:
        """
        Combines all the above methods to be used as one command.
        Takes the details and the statistics data and loads it into dbsqlite.
        It also returns a combination of the data as a dictionary.
        """

        raw_data = self._extract_data(account_id=account_id, application_id=application_id, realm=realm)
        details = self._parse_details_data(raw_data, account_id=account_id)
        statistics = self._parse_statistics_data(raw_data, account_id=account_id)

        if load_to_db:
            DataModelLoader.insert(PlayerPersonalDataDetailsModel, details, db_path=db_path)
            DataModelLoader.insert(PlayerPersonalDataStatisticsModel, statistics, db_path=db_path)

        # Return the dict with combined data
        result = [{
            "details": details,
            "statistics": statistics
        }]

        return result
