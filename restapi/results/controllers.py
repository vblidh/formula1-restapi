from typing import List
from restapi.db import session
from restapi.models import Qualifying, Result, Race

from sqlalchemy.orm import joinedload


def get_results_from_race(race_id):
    results = session.query(Result).filter(Result.raceId == race_id).options(
        joinedload('driver'), joinedload('constructor'), joinedload('status')).order_by(Result.position).all()
    return results


def get_team_result(race_id, constructor_id):
    results = session.query(Result).filter(Result.raceId == race_id, Result.constructorId == constructor_id).options(
        joinedload('driver')).all()
    return results


def get_results_from_races(race_ids):
    results = session.query(Result).join(Race).filter(
        Result.raceId.in_(race_ids)).options(
            joinedload('driver'),
            joinedload('constructor'),
            joinedload('race'),
            joinedload('status')
    ).order_by(
        Race.round.desc(),
        Result.position).all()
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
