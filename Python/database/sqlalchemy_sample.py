#!/usr/bin/env python3

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///test_sqlite_player.db", echo=True)
Base = declarative_base()


########################################################################
class Player(Base):
    """"""
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    lastname = Column(String)
    position = Column(String)
    club = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, lastname, position, club):
        """"""
        self.lastname = lastname
        self.position = position
        self.club = club


def create_table():
    # create tables
    Base.metadata.create_all(engine)


def insert_data():
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create objects
    p1 = Player("Buffon", "Goalkeeper", "Juventus")
    session.add(p1)

    p2 = Player("Chiellini", "Defender", "Juventus")
    session.add(p2)

    p3 = Player("Dybala", "Forward", "Juventus")
    session.add(p3)

    # commit the record the database
    session.commit()


def query_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    # query objects
    for player in session.query(Player).order_by(Player.id):
        print("Player:", player.lastname, player.position)


if __name__ == "__main__":
    create_table()
    insert_data()
    query_data()
