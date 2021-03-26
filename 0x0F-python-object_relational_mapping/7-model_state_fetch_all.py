#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

connInfo = 'mysql+mysqldb://{}:{}@localhost/{}'
engine = create_engine(connInfo.format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]),
                       pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()
states = session.query(State).order_by(State.id.asc()).all()
for row in states:
    print(str(row.id) + ": " + row.name)
