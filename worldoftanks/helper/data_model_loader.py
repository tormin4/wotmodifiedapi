import os
import logging
from sqlalchemy.orm import sessionmaker

from worldoftanks.helper.create_engine import create_db_engine


class DataModelLoader:

    @staticmethod
    def insert(model: object, data: list):
        """
        Generic method to insert a data model into sqlite.
        """

        try:
            s = sessionmaker(bind=create_db_engine(path=os.getcwd()))
            session = s()
            session.bulk_insert_mappings(model, data)
            session.commit()
            session.close()
            logging.info('Player vehicles data Loaded into database')

        except:
            # TODO: Create a less generic exception
            logging.error('Player vehicles data loading data failed')
            raise

    @staticmethod
    def check_if_data_exists(model: object,):
        """
        Checks if any data is existing in the table.
        """
        s = sessionmaker(bind=create_db_engine(path=os.getcwd()))
        session = s()
        table_values = session.query(model).count()

        if table_values > 0:
            return True
        else:
            return False
