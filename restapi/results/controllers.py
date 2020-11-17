from typing import List
from restapi.db import session
from restapi.models import ConstructorResult, Driver, Qualifying, Result, Race

from sqlalchemy.orm import joinedload


def get_results_from_race(race_id):
    results = session.query(Result).filter(Result.raceId == race_id).options(
        joinedload('driver'), joinedload('constructor'), joinedload('status')).order_by(Result.position).all()
    return results


def get_team_result(race_id, constructor_id):
    results = session.query(Result).filter(Result.raceId == race_id, Result.constructorId == constructor_id).options(
        joinedload('driver')).all()
    return results


def get_constructor_results_by_race(race_id):
    return session.query(ConstructorResult).filter(ConstructorResult.raceId == race_id).order_by(ConstructorResult.points.desc()).all()


def get_last_results_of_driver(driver_id, start, stop):  
    total_count = session.query(Result).filter(Result.driverId == driver_id).count()
    results = session.query(Result).filter(Result.driverId == driver_id).options(joinedload('status'), joinedload('race')
    ).join(Race).order_by(Race.date.desc()).slice(start, stop).all()
    return total_count, results


def get_results_from_races(race_ids):
    results = session.query(Result).join(Race).filter(
        Result.raceId.in_(race_ids)).options(
            joinedload('driver'),
            joinedload('constructor'),
            joinedload('race'),
            joinedload('status')
    ).order_by(
        Race.round.desc(),
        Result.positionOrder).all()
    return results


def get_qualifying_results(race_ids):
    if isinstance(race_ids, int):
        qualies = session.query(Qualifying).filter(
            Qualifying.raceId == race_ids).options(
                joinedload('driver'),
                joinedload('constructor'),
                joinedload('race')
        ).order_by(Qualifying.position).all()
    elif isinstance(race_ids, list):
        qualies = session.query(Qualifying).join(Race).filter(
            Qualifying.raceId.in_(race_ids)).options(
                joinedload('driver'),
                joinedload('constructor'),
                joinedload('race')
        ).order_by(
            Race.round.desc(),
            Qualifying.position).all()
    else:
        qualies = []
    return qualies

def get_all_driver_results(driver_id):
    return session.query(Result).join(Driver).filter(Driver.driverId==driver_id).all()

def get_all_driver_poles(driver_id):
    return session.query(Qualifying).join(Driver).filter(Driver.driverId==driver_id, Qualifying.position==1).all()