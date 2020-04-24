import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime

Base = declarative_base()


class PlayerPersonalDataDetailsModel(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'player_personal_details'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_battle_time = Column(Integer)
    account_id = Column(String)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    gold = Column(Integer)
    free_xp = Column(Integer)
    ban_time = Column(Integer)
    is_bound_to_phone = Column(Integer)
    is_premium = Column(Boolean)
    credits = Column(Integer)
    premium_expires_at = Column(Integer)
    bonds = Column(Integer)
    battle_life_time = Column(Integer)
    global_rating = Column(Integer)
    clan_id = Column(Integer)


class PlayerPersonalDataStatisticsModel(Base):
    """
    Create data model for player personal statistics data.
    """
    __tablename__ = 'player_personal_statistics'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    statistic_type = Column(String)
    spotted = Column(Integer)
    battles_on_stunning_vehicles = Column(Integer)
    avg_damage_blocked = Column(Float)
    direct_hits_received = Column(Integer)
    explosion_hits = Column(Integer)
    piercings_received = Column(Integer)
    piercings = Column(Integer)
    max_damage_tank_id = Column(String)
    max_xp_tank_id = Column(String)
    max_frags = Column(Integer)
    xp = Column(Integer)
    survived_battles = Column(Integer)
    dropped_capture_points = Column(Integer)
    hits_received = Column(Integer)
    hits_percents = Column(Integer)
    max_damage = Column(Integer)
    draws = Column(Integer)
    battles = Column(Integer)
    damage_received = Column(Integer)
    avg_damage_assisted = Column(Float)
    avg_damage_assisted_track = Column(Float)
    frags = Column(Integer)
    stun_number = Column(Integer)
    avg_damage_assisted_radio = Column(Float)
    capture_points = Column(Integer)
    stun_assisted_damage = Column(Integer)
    hits = Column(Integer)
    battle_avg_xp = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    damage_dealt = Column(Integer)
    no_damage_direct_hits_received = Column(Integer)
    shots = Column(Integer)
    explosion_hits_received = Column(Integer)
    tanking_factor = Column(Integer)
    max_frags_tank_id = Column(Integer)


class PlayerPersonalVehiclesModel(Base):
    """
    Create data model for the personal vehicles statistics.
    """
    __tablename__ = 'player_vehicles'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    tank_id = Column(String)
    battles = Column(Integer)
    mark_of_mastery = Column(Integer)


class DataModel:

    @staticmethod
    def create_tables(engine):
        Base.metadata.create_all(engine)

