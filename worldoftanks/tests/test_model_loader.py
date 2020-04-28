import unittest
from sqlalchemy import create_engine

from worldoftanks.orm.data_model import Base, DataModel, PlayerPersonalDataDetailsModel
from worldoftanks.helper.data_model_loader import DataModelLoader

data = [{"id": 1}, {"id": 2}]


class TestDataModelLoader(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')

    def test_db_setUp(self):
        DataModel.create_tables(self.engine)

    def test_multiple_insert(self):
        DataModelLoader.insert(PlayerPersonalDataDetailsModel, data, db_engine=self.engine, db_path='')

    def test_supply_data_count(self):
        result = DataModelLoader.check_if_data_exists(PlayerPersonalDataDetailsModel, db_engine=self.engine, db_path='')
        expected = True
        self.assertEqual(result, expected)

    def test_xdb_tearDown(self):
        # The 'zdb' is not a typo. The database still needs to be available for the rest of the tests to run.
        # The unittest module is taking the methods in an alphabetical order so it had to be prefixed with a "z".
        Base.metadata.drop_all(self.engine)