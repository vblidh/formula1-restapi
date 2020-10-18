from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from .app import app

engine = create_engine("sqlite:///formula1_database.db", echo=True,pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
