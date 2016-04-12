from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///list-comprehender.db", echo=True)

Base = declarative_base()


class Test(Base):

    __tablename__ = "tests"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    difficulty = Column(String)

    statistic = relationship("Statistic", uselist=False, back_populates="statistics")

    def __repr__(self):
        return "Question: %s" % self.question


class Statistic(Base):

    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("tests.id"))
    correct = Column(Integer)
    incorrect = Column(Integer)

    question = relationship("Test", back_populates="tests")

    def __repr__(self):
        return "Statistics for %" % self.question.question
