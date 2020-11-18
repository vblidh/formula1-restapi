from restapi.db import session
from restapi.models import Driver


def get_drivers():
    return session.query(Driver).order_by(Driver.dob.desc()).all()


def get_driver(id):
    return session.query(Driver).filter(Driver.driverId == id).one_or_none()


def get_driver_by_code(code):
    return session.query(Driver).filter(Driver.code == code).all()

