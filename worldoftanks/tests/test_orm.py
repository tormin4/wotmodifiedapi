import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from worldoftanks.orm.data_model import Base, DataModel
from worldoftanks.orm.data_model import PlayerPersonalDataDetailsModel, PlayerPersonalDataStatisticsModel, \
    PlayerPersonalVehiclesModel, TankopediaInfoModel, TankopediaAchievementsModel, \
    TankopediaVehiclesModel, TankopediaMapsModel, VehiclesStatisticsModel, VehiclesFragsModel, VehiclesAchievements


test_data = {"id": 10, "account_id": "1234"}


class TestModels(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def test_db_setUp(self):
        DataModel.create_tables(self.engine)
        # Add all the data into the models here to be evaluated in the methods below.
        self.session.add(PlayerPersonalDataDetailsModel(id=test_data['id'], account_id=test_data['account_id']))
        self.session.add(PlayerPersonalDataStatisticsModel(id=test_data['id']))
        self.session.add(PlayerPersonalVehiclesModel(id=test_data['id']))
        self.session.add(TankopediaInfoModel(id=test_data['id']))
        self.session.add(TankopediaAchievementsModel(id=test_data['id']))
        self.session.add(TankopediaVehiclesModel(id=test_data['id']))
        self.session.add(TankopediaMapsModel(id=test_data['id']))
        self.session.add(VehiclesStatisticsModel(id=test_data['id']))
        self.session.add(VehiclesFragsModel(id=test_data['id']))
        self.session.add(VehiclesAchievements(id=test_data['id']))
        self.session.commit()

    def test_player_personal_details_model(self):
        expected = PlayerPersonalDataDetailsModel(id=test_data['id'], account_id=test_data['account_id'])
        query = self.session.query(PlayerPersonalDataDetailsModel).first()
        self.assertEqual(query.account_id, expected.account_id)

    def test_player_personal_statistics_model(self):
        expected = PlayerPersonalDataStatisticsModel(id=test_data['id'])
        query = self.session.query(PlayerPersonalDataStatisticsModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_player_personal_vehicles_model(self):
        expected = PlayerPersonalVehiclesModel(id=test_data['id'])
        query = self.session.query(PlayerPersonalVehiclesModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_tankopedia_information_model(self):
        expected = TankopediaInfoModel(id=test_data['id'])
        query = self.session.query(TankopediaInfoModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_tankopedia_achievements_model(self):
        expected = TankopediaAchievementsModel(id=test_data['id'])
        query = self.session.query(TankopediaAchievementsModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_tankopedia_vehicles_model(self):
        expected = TankopediaVehiclesModel(id=test_data['id'])
        query = self.session.query(TankopediaVehiclesModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_tankopedia_maps_model(self):
        expected = TankopediaMapsModel(id=test_data['id'])
        query = self.session.query(TankopediaMapsModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_vehicle_statistics_model(self):
        expected = VehiclesStatisticsModel(id=test_data['id'])
        query = self.session.query(VehiclesStatisticsModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_vehicle_frags_model(self):
        expected = VehiclesFragsModel(id=test_data['id'])
        query = self.session.query(VehiclesFragsModel).first()
        self.assertEqual(query.id,  expected.id)

    def test_vehicle_achievement_model(self):
        expected = VehiclesAchievements(id=test_data['id'])
        query = self.session.query(VehiclesAchievements).first()
        self.assertEqual(query.id,  expected.id)

    def test_xdb_tearDown(self):
        # The 'zdb' is not a typo. The database still needs to be available for the rest of the tests to run.
        # The unittest module is taking the methods in an alphabetical order so it had to be prefixed with a "z".
        Base.metadata.drop_all(self.engine)
