from restapi.db import session
from restapi.models import Race

from sqlalchemy import func, over
from sqlalchemy.orm import joinedload


def get_race(year, round):
    return session.query(Race).filter(Race.year == year, Race.round == round).options(joinedload('circuit')).one_or_none()


def get_races_in_year(year):
    return session.query(Race).filter(Race.year == year).order_by(Race.round).all()


def get_all_races():
    return session.query(Race).options(joinedload('circuit')).all()


def get_last_race():
    subq = session.query(func.max(Race.raceId))
    return session.query(Race).filter(Race.raceId == subq).one_or_none()

def get_id_of_last_race_of_years():
    subq = session.query(Race.raceId, Race.round, func.max(Race.round).over(
        partition_by=Race.year).label('last_round')).subquery()
    race_ids = session.query(subq.c.raceId).filter(
        subq.c.round == subq.c.last_round).all()
    return race_ids
