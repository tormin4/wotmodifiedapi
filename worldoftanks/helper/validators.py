import logging


class Validators:

    @staticmethod
    def check_if_param_exists(param: str, param_type: str):
        """
        Checks if the token / account_id / application id has been provided.
        """

        try:
            len(param)
        except ValueError:
            logging.error("World of Tanks {} has not been provided".format(param_type))
            raise ValueError("World of Tanks {} has not been provided".format(param_type))
