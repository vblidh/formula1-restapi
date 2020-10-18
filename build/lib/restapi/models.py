# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text, text, String
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Circuit(Base):
    __tablename__ = 'circuits'

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    location = Column(Text, nullable=False)
    country = Column(Text, nullable=False)
    lat = Column(Text)
    lng = Column(Text)
    alt = Column(Text)
    url = Column(Text)

    def to_json(self):
        return {
            "ref": self.circuitRef,
            "name": self.name,
            "city": self.name,
            "country": self.name,
        }


class Constructor(Base):
    __tablename__ = 'constructors'

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(Text, nullable=False, server_default=text("\"\""))
    name = Column(Text, nullable=False, unique=True,
                  server_default=text("\"\""))
    nationality = Column(Text)
    url = Column(Text, nullable=False)

    def to_json(self):
        return {
            "ref": self.constructorRef,
            "name": self.name,
            "country": self.nationality,
        }


class Driver(Base):
    __tablename__ = 'drivers'

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(Text, nullable=False)
    number = Column(Integer, nullable=False)
    code = Column(String(3))
    forename = Column(String(30))
    surname = Column(String(30))
    dob = Column(String(20))
    nationality = Column(String(15))
    url = Column(String(20))

    def to_json(self):
        return {
            "id": self.driverId,
            "number": self.number,
            "code": self.code,
            "first_name": self.forename,
            "last_name": self.surname,
            "date_of_birth": self.dob,
            "nationality": self.nationality,
            "wiki_url": self.url
        }


class Race(Base):
    __tablename__ = 'races'

    raceId = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    circuitId = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)
    time = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)

    def to_json(self):
        return {
            "year": self.year,
            "round": self.round,
            "name": self.name,
            "date": self.date,
            "time_of_day": self.time,
        }


class Season(Base):
    __tablename__ = 'seasons'

    year = Column(Integer, primary_key=True)
    url = Column(Text)

    def to_json(self):
        return {
            "year": self.year,
            "wiki_url": self.url
        }


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer)
    status = Column(NullType, primary_key=True)


class ConstructorResult(Base):
    __tablename__ = 'constructor_results'

    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'), nullable=False)
    constructorId = Column(ForeignKey(
        'constructors.constructorId'), nullable=False)
    points = Column(Integer)
    status = Column(NullType)

    constructor = relationship('Constructor')
    race = relationship('Race')

    def to_json(self):
        return {
         "race" : self.race.to_json(),
         "team" : self.constructor.to_json(),
         "points" : self.points,
         "status" : self.status   
        }

class ConstructorStanding(Base):
    __tablename__ = 'constructor_standings'

    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'), nullable=False)
    constructorId = Column(ForeignKey(
        'constructors.constructorId'), nullable=False)
    points = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
    positionText = Column(Text)
    wins = Column(Integer, nullable=False)

    constructor = relationship('Constructor')
    race = relationship('Race')

    def to_json(self):
        return {
            "race": self.race.to_json(),
            "team": self.constructor.to_json(),
            "points": self.points,
            "position": self.position,
            "wins" : self.wins
        }


class DriverStanding(Base):
    __tablename__ = 'driver_standings'

    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'), nullable=False)
    driverId = Column(ForeignKey('drivers.driverId'), nullable=False)
    points = Column(Integer)
    position = Column(Integer)
    positionText = Column(Text)
    wins = Column(Integer)

    driver = relationship('Driver')
    race = relationship('Race')

    def to_json(self):
        return {
            "race" : self.race.to_json(),
            "driver": self.driver.to_json(),
            "points" : self.points,
            "position" : self.position,
            "wins" : self.wins
        }

class LapTime(Base):
    __tablename__ = 'lap_times'

    raceId = Column(ForeignKey('races.raceId'),
                    primary_key=True, nullable=False)
    driverId = Column(ForeignKey('drivers.driverId'),
                      primary_key=True, nullable=False)
    lap = Column(Integer, primary_key=True, nullable=False)
    position = Column(Integer)
    time = Column(Text)
    milliseconds = Column(Text)

    driver = relationship('Driver')
    race = relationship('Race')


class PitStop(Base):
    __tablename__ = 'pit_stops'

    raceId = Column(ForeignKey('races.raceId'),
                    primary_key=True, nullable=False)
    driverId = Column(ForeignKey('drivers.driverId'),
                      primary_key=True, nullable=False)
    stop = Column(Integer, primary_key=True, nullable=False)
    lap = Column(Integer, nullable=False)
    time = Column(Text, nullable=False)
    duration = Column(Text, nullable=False)
    milliseconds = Column(Text)

    driver = relationship('Driver')
    race = relationship('Race')


class Qualifying(Base):
    __tablename__ = 'qualifying'

    qualifyId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'), nullable=False)
    driverId = Column(ForeignKey('drivers.driverId'), nullable=False)
    constructorId = Column(ForeignKey(
        'constructors.constructorId'), nullable=False)
    number = Column(Integer)
    position = Column(Integer, nullable=False)
    q1 = Column(Text)
    q2 = Column(Text)
    q3 = Column(Text)

    constructor = relationship('Constructor')
    driver = relationship('Driver')
    race = relationship('Race')

    def to_json(self):
        return {
            "race": self.race.to_json(),
            "driver": self.driver.to_json(),
            "team": self.constructor.to_json(),
            "position": self.position,
            "Q1": self.q1,
            "Q2" : self.q2,
            "Q3" : self.q3
        }


class Result(Base):
    __tablename__ = 'results'

    resultId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'))
    driverId = Column(ForeignKey('drivers.driverId'))
    constructorId = Column(ForeignKey('constructors.constructorId'))
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionText = Column(Text)
    positionOrder = Column(Text)
    points = Column(Integer)
    laps = Column(Integer)
    time = Column(Text)
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer)
    fastestLapTime = Column(Text)
    fastestLapSpeed = Column(Numeric)
    statusId = Column(ForeignKey('status.statusId'))

    constructor = relationship('Constructor')
    driver = relationship('Driver')
    race = relationship('Race')
    status = relationship('Status')

    def to_json(self):
        return {
            "race": self.race.to_json(),
            "driver": self.driver.to_json(),
            "team" : self.constructor.to_json(),
            "grid": self.grid,
            "position": self.position,
            "laps": self.laps,
            "time": self.time,
            "fastest_lap": self.fastestLap,
            "fastest_lap_time": self.fastestLapTime,
            "fastest_lap_speed": self.fastestLapSpeed,
            "status": self.status.status
        }
