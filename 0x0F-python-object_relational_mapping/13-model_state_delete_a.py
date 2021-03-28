#!/usr/bin/python3
""" Description module """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    connInfo = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
                            connInfo.format(sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3]),
                            pool_pre_ping=True)
    session = Session(engine)
    Base = declarative_base()
    query = session.query(State).filter(State.name.ilike("%a%")).all()
    for item in query:
        session.delete(item)
    session.commit()