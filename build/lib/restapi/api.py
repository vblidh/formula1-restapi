from .db import session

from .models import (
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


def get_circuits():
    circuits = session.query(Circuit).all()
    return circuits

def get_circuit(id):
    return session.query(Circuit).filter(Circuit.circuitId==id).one_or_none()

def get_drivers():
    return session.query(Driver).all()

def get_driver(id):
    return session.query(Driver).filter(Driver.driverId==id).one_or_none()

def get_driver_by_code(code):
    return session.query(Driver).filter(Driver.code==code).one_or_none()

def get_teams():
    return session.query(Constructor).all()

def get_team(id):
    return session.query(Constructor).filter(Constructor.constructorId==id).one_or_none()

def get_constructor_results_by_race(race_id):
    return session.query(ConstructorResult).filter(ConstructorResult.raceId==race_id).all()

def get_constructor_standings_from_race(race_id):
    return session.query(ConstructorStanding).filter(ConstructorStanding.raceId==race_id).all()

def get_driver_standings_by_race(driver_id, race_id):
    return session.query(DriverStanding).filter(DriverStanding.driverId==driver_id, DriverStanding.raceId==race_id).all()

def get_races_in_year(year):
    return session.query(Race).filter(Race.year==year)

def get_race(year, round):
    return session.query(Race).filter(Race.year==year, Race.round==round).one_or_none()

def get_all_races():
    return session.query(Race).all()

def get_results_from_race(race_id):
    results = session.query(Result).filter(Result.raceId==race_id).all()
    return results

def get_qualifying_results_by_race(race_id):
    qualies = session.query(Qualifying).filter(Qualifying.raceId==race_id).all()
    return qualies