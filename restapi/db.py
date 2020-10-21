import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from restapi import app

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], connect_args={
    "check_same_thread": False}, echo=True, poolclass=StaticPool)
Session = sessionmaker(bind=engine)
session = Session()
