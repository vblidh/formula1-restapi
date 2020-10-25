from restapi.db import session
from restapi.models import (
    Circuit,
    Driver,
    Constructor,
    ConstructorResult,
    ConstructorStanding,
    DriverStanding,
    PitStop,
    Qualifying,
    Race,
    Result,
    Status,
)

from sqlalchemy.orm import joinedload
from sqlalchemy import over, func




def get_teams():
    return session.query(Constructor).all()


def get_team(id):
    return session.query(Constructor).filter(Constructor.constructorId == id).one_or_none()


def get_constructor_results_by_race(race_id):
    return session.query(ConstructorResult).filter(ConstructorResult.raceId == race_id).order_by(ConstructorResult.points.desc()).all()






def get_results_from_race(race_id, loadRelations=False):
    # TODO Make a big query on all races of a season
    if loadRelations:
        results = session.query(Result).filter(Result.raceId == race_id).options(
            joinedload('driver'), joinedload('constructor')).order_by(Result.position).all()
    else:
        results = session.query(Result).filter(Result.raceId == race_id).all()
    return results



