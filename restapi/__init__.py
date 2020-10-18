from flask import Flask
from restapi.appgenerator import create_app

print("Creating app")
app = create_app()
import restapi.endpoints