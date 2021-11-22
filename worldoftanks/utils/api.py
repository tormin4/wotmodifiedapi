import requests
import logging
import time


class API:

    def __init__(self, application_id: str, account_id: str, realm: str):
        self.account_id = account_id
        self.application_id = application_id
        self.realm = realm
        self.BASE_URL = 'https://api.worldoftanks.{}/wot'.format(realm)
        self.MAX_ATTEMPTS = 3
        self.BACKOFF_MULTIPLIER = 10

    def get_data(self, source: str):
        """
        Generic method to extract data for an endpoint and validate the result
        """

        if source == 'player_personal_data':
            url = self._build_url_player_personal()
        elif source == 'player_vehicles_data':
            url = self._build_url_player_vehicles()
        elif source == 'player_achievements':
            url = self._build_url_player_achievements()
        elif source == 'tankopedia_vehicles':
            url = self._build_url_tankopedia_vehicles()
        elif source == 'tankopedia_achievements':
            url = self._build_url_tankopedia_achievements()
        elif source == 'tankopedia_info':
            url = self._build_url_tankopedia_information()
        elif source == 'tankopedia_maps':
            url = self._build_url_tankopedia_maps()
        elif source == 'vehicle_statistics':
            url = self._build_url_vehicle_statistics()
        elif source == 'vehicle_achievements':
            url = self._build_url_vehicle_achievements()
        elif source == 'tankopedia_badges':
            url = self._build_url_tankopedia_badges()
        else:
            raise ValueError('API Method invalid')

        attempt = 0
        while attempt <= self.MAX_ATTEMPTS:
            attempt += 1

            r = requests.get(url)
            if self._eval_response(r, attempt):
                return r.json()
            else:
                continue

    def _build_url_tankopedia_badges(self) -> str:
        """
        Extracts tankopedia badges.
        """

        url = "{}/encyclopedia/badges/?application_id={}" \
            .format(self.BASE_URL, self.application_id)

        return url

    def _build_url_vehicle_statistics(self) -> str:
        """
        Extracts vehicles statistics in the player vehicle section.
        """

        url = "{}/tanks/stats/?application_id={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.account_id)

        return url

    def _build_url_vehicle_achievements(self) -> str:
        """
        Extracts vehicles statistics in the player vehicle section.
        """

        url = "{}/tanks/achievements/?application_id={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.account_id)

        return url

    def _build_url_player_personal(self) -> str:
        """
        Extracts player personal data from the accounts section.
        """

        url = "{}/account/info/?application_id={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.account_id)

        return url

    def _build_url_player_vehicles(self) -> str:
        """
        Extracts player vehicle data from the accounts section.
        """

        url = "{}/account/tanks/?application_id={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.account_id)

        return url

    def _build_url_player_achievements(self) -> str:
        """
        Extracts player achievements data from the accounts section.
        """
        url = "{}/account/achievements/?application_id={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.account_id)

        return url

    def _build_url_tankopedia_vehicles(self) -> str:
        """
        Extracts tankopedia vehicles data from the accounts section.
        """

        url = "{}/encyclopedia/vehicles/?application_id={}" \
            .format(self.BASE_URL, self.application_id)

        return url

    def _build_url_tankopedia_achievements(self) -> str:
        """
        Extracts tankopedia achievements data from the accounts section.
        """
        url = "{}/encyclopedia/achievements/?application_id={}" \
            .format(self.BASE_URL, self.application_id)

        return url

    def _build_url_tankopedia_information(self) -> str:
        """
        Builds the url to extract tankopedia information data.
        """
        url = "{}/encyclopedia/info/?application_id={}" \
            .format(self.BASE_URL, self.application_id)

        return url

    def _build_url_tankopedia_maps(self) -> str:
        """
        Builds the url to extract tankopedia maps data.
        """
        url = "{}/encyclopedia/arenas/?application_id={}" \
            .format(self.BASE_URL, self.application_id)

        return url

    def _eval_response(self, response, attempt: int) -> bool:
        """
        Evaluates the status code of the get request
        """

        if response.status_code == 200:
            # ToDO: This needs a better implementation
            # Check the response for the correct responses.

            try:
                message = response.json()['error']['message']
                code = response.json()['error']['code']
            except:
                logging.info('API call success: Status Code 200')
                message = None
                code = None

            if message and code:
                logging.error("HTTP Response Code: {} - Message: {}".format(code, message))
                raise ConnectionError("HTTP Response Code: {} - Message: {}".format(code, message))
            else:
                return True

        if response.status_code != 200:
            waiting_seconds = attempt * self.BACKOFF_MULTIPLIER
            logging.warning("HTTP Error Code: {} - Attempt: {} - Will retry again in {}"
                            .format(response.status_code, attempt, attempt * self.BACKOFF_MULTIPLIER))
            time.sleep(waiting_seconds)
