from sqlalchemy import create_engine


def create_db_engine(path: str):
    """
    Creates a sqlite database to be populated by the ORM
    """
    engine = create_engine('sqlite:///{}/world_of_tanks.db'.format(path))

    return engine
