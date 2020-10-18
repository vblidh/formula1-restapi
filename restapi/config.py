import os

SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL", 'sqlite:///formula1_database.db')
DEBUG=True
SECRET_KEY = '\xebSh0P\x84.\x01\xf8\xeb\xf7\xddF\xf2>\xc7'
JSON_AS_ASCII=False