from restapi.models import LapTime
from restapi.db import session


def get_laptimes(race_id):
    laptimes = session.query(LapTime).filter(LapTime.raceId == race_id).order_by(LapTime.lap, LapTime.time).all()
    return laptimes