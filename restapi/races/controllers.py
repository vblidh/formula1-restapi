from restapi.db import session
from restapi.models import Race

from sqlalchemy import func, over
from sqlalchemy.orm import joinedload
from datetime import date


def get_race(year, round):
    return session.query(Race).filter(Race.year == year, Race.round == round).options(joinedload('circuit')).one_or_none()

def get_race_by_id(id):
    return session.query(Race).filter(Race.raceId == id).one_or_none()

def get_races_in_year(year):
    return session.query(Race).filter(Race.year == year).order_by(Race.round).all()


def get_all_races():
    return session.query(Race).options(joinedload('circuit')).all()


def get_races_in_circuit(circuit_id:int, start:int, end:int, include_upcoming:bool=True):
    if include_upcoming:
        count = session.query(Race).filter(Race.circuitId == circuit_id).count()
        if end:
            races = session.query(Race).options(joinedload('circuit')).filter(Race.circuitId == circuit_id).order_by(Race.date.desc()).slice(start, end).all()
        else:
            races = session.query(Race).options(joinedload('circuit')).filter(Race.circuitId == circuit_id).order_by(Race.date.desc()).all()
        return count, races
    else:
        now = date.today()
        count = session.query(Race).filter(
            Race.circuitId == circuit_id, Race.date < str(now)).count()
        if end:
            races = session.query(Race).options(joinedload('circuit')).filter(
                Race.circuitId == circuit_id, Race.date < str(now)).order_by(Race.date.desc()).slice(start, end).all()
        else:
            races = session.query(Race).options(joinedload('circuit')).filter(
                Race.circuitId == circuit_id, Race.date < str(now)).order_by(Race.date.desc()).all()
        return count, races


def get_last_race():
    subq = session.query(func.max(Race.raceId))
    return session.query(Race).filter(Race.raceId == subq).one_or_none()


def get_last_race_of_years(year=0):
    if year == 0:
        subq = session.query(Race, func.max(Race.round).over(
            partition_by=Race.year).label('last_round')).subquery()
        res = session.query(subq).filter(
            subq.c.round == subq.c.last_round).all()
    elif year > 1949 and year < 2021:
        res = session.query(Race).filter(
            Race.year == year).order_by(Race.round.desc()).first()
    else:
        res = []
    return res
