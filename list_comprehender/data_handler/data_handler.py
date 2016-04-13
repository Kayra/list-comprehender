from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from list_comprehender.data_handler import models

Session = sessionmaker(bind=models.engine)

session = Session()


def createTables():
    models.Base.metadataModel.create_all(models.engine)


def tablesExist():
    return models.engine.dialect.has_table(models.engine.connect(), "tests") and models.engine.dialect.has_table(models.engine.connect(), "statistics")


def retrieve_random_test(difficulty):
    return session.query(models.Test).filter(models.Test.difficulty == difficulty).order_by(func.random()).limit(1)
