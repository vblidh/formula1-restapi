from sqlalchemy.orm import joinedload
from sqlalchemy import func

from restapi.db import session
from restapi.models import ConstructorStanding, DriverStanding, Race


def get_current_driver_standings():
    subq = session.query(func.max(DriverStanding.raceId))
    return session.query(DriverStanding).filter(DriverStanding.raceId == subq).options(joinedload('race'), joinedload('driver')).order_by(DriverStanding.position).all()


def get_individual_standing(standing_id):
    return session.query(DriverStanding).filter(DriverStanding.driverStandingsId == standing_id).one_or_none()


def get_driver_standings_by_race(race_id):
    return session.query(DriverStanding).filter(DriverStanding.raceId == race_id).options(joinedload('driver')).order_by(DriverStanding.position).all()


def get_driver_standings_by_races(race_ids):
    return session.query(DriverStanding).join(Race).filter(
        DriverStanding.raceId.in_(race_ids)
    ).options(joinedload('driver')
              ).order_by(
        Race.round.desc(),
        DriverStanding.position
    ).all()


def get_constructor_standings_from_race(race_id):
    return session.query(ConstructorStanding).filter(ConstructorStanding.raceId == race_id).order_by(ConstructorStanding.position).all()


def get_constructor_standings_from_races(race_ids):
    return session.query(ConstructorStanding).join(Race).filter(
        ConstructorStanding.raceId.in_(race_ids)
    ).options(joinedload('constructor')
              ).order_by(
        Race.round.desc(),
        ConstructorStanding.position).all()


def get_constructor_standings_from_races_by_team(race_ids, constructor_id):
    return session.query(ConstructorStanding).filter(ConstructorStanding.constructorId == constructor_id, ConstructorStanding.raceId.in_(race_ids)).options(joinedload('race')).all()
