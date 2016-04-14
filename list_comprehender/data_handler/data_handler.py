from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

from list_comprehender.data_handler import models

Session = sessionmaker(bind=models.engine)

session = Session()


def createTables():
    models.Base.metadata.create_all(models.engine)


def addData():
    test = models.Test(question="targets = []\nfor follower in followers:\n\ttargets.append(follower)", answer="[follower for follower in followers]", difficulty="easy")
    session.add(test)
    session.commit()


def retrieve_random_test(difficulty):
    return session.query(models.Test).filter(models.Test.difficulty == difficulty).order_by(func.random()).first()
