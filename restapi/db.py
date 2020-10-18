import os
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

engine = create_engine('sqlite:///formula1_database.db', connect_args={
    "check_same_thread": False}, echo=True, poolclass=StaticPool)
Session = sessionmaker(bind=engine)
session = Session()
