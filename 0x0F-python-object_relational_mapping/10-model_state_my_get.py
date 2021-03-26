#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine, Table
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import text
import sys

connInfo = 'mysql+mysqldb://{}:{}@localhost/{}'
engine = create_engine(connInfo.format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]),
                       pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
if len(sys.argv) != 5:
    print("Not found")
else:
    query = session.query(State).filter(State.name == sys.argv[4]).all()
    for e in query:
        print("{}".format(e.id))
