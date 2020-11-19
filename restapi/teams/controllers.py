from sqlalchemy.orm import joinedload
from restapi.db import session

from restapi.models import Constructor, Result, Race

def get_team_by_id(id):
    return session.query(Constructor).filter(Constructor.constructorId == id).one_or_none()


def get_all_teams():
    return session.query(Constructor).all()


def get_team_of_driver_in_races(driver_id, race_ids):
    results = session.query(Result).join(Race).options(joinedload('constructor')).filter(
        Result.driverId == driver_id, Result.raceId.in_(race_ids)).order_by(Race.date.desc()).all()
    teams = [r.constructor for r in results]
    return teams
