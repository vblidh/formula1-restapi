from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


engine = create_engine("sqlite:///formula1_database.db", echo=True,pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()
