import requests
import logging
import time


class API:

    def __init__(self, application_id: str, account_id: str, token: str):
        self.account_id = account_id
        self.application_id = application_id
        self.access_token = token
        self.BASE_URL = 'https://api.worldoftanks.eu/wot'
        self.MAX_ATTEMPTS = 3
        self.BACKOFF_MULTIPLIER = 10

    def get_data(self, source: str):
        """
        Generic method to extract data for an endpoint and validate the result
        """

        if source == 'player_personal_data':
            url = self.build_url_player_personal()
        elif source == 'player_vehicles_data':
            url = self.build_url_player_vehicles()
        else:
            raise ValueError('API Method invalid')

        attempt = 0
        while attempt <= self.MAX_ATTEMPTS:
            attempt += 1

            r = requests.get(url)
            if self._eval_response(r, url, attempt):
                return r.json()
            else:
                continue

    def build_url_player_personal(self) -> str:
        """
        Extracts player personal data from the accounts section.
        """

        url = "{}/account/info/?application_id={}&access_token={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.access_token, self.account_id)

        return url

    def build_url_player_vehicles(self) -> str:
        """
        Extracts player vehicle data from the accounts section.
        """

        url = "{}/account/tanks/?application_id={}&access_token={}&account_id={}" \
            .format(self.BASE_URL, self.application_id, self.access_token, self.account_id)

        return url

    def _eval_response(self, response, url, attempt: int) -> bool:
        """
        Evaluates the status code of the get request
        """

        # TODO: Create more descriptive error handling on different error codes.

        if response.status_code == 200:
            logging.info('API call success: Status Code 200')
            return True

        if response.status_code != 200:
            waiting_seconds = attempt * self.BACKOFF_MULTIPLIER
            logging.warning("Endpoint: {} HTTP Error Code: {} - Attempt: {} - Will retry again in {}"
                            .format(url, response.status_code, attempt, attempt * self.BACKOFF_MULTIPLIER))
            time.sleep(waiting_seconds)
