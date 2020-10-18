import os

SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL", 'sqlite:///formula1_database.db')
DEBUG=True
FLASK_ENV='development'
SECRET_KEY = '\xebSh0P\x84.\x01\xf8\xeb\xf7\xddF\xf2>\xc7'