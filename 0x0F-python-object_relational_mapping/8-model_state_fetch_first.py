#!/usr/bin/python3
"""Module that retrieves and prints first"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    stateo = session.query(State).order_by(State.id).first()
    if stateo != None:
        print("{}: {}".format(stateo.id, stateo.name))
    else:
        print("Nothing")
