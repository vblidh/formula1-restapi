import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

session = None

def init_db(app):
    global session
    # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], connect_args={
    #     "check_same_thread": False}, echo=True, poolclass=StaticPool)
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
