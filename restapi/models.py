# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text, text, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Circuit(Base):
    __tablename__ = 'circuits'

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String(15), nullable=False)
    name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    lat = Column(String(30))
    lng = Column(String(30))
    alt = Column(String(30))
    url = Column(String(30))

    def to_json(self):
        return {
            "ref": self.circuitRef,
            "name": self.name,
            "city": self.location,
            "country": self.country,
            "wiki_url" : self.url,
        }


class Constructor(Base):
    __tablename__ = 'constructors'

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String(30), nullable=False,
                            server_default=text("\"\""))
    name = Column(String(40), nullable=False, unique=True,
                  server_default=text("\"\""))
    nationality = Column(String(30))
    url = Column(String(50), nullable=False)

    def to_json(self):
        return {
            "ref": self.constructorRef,
            "name": self.name,
            "country": self.nationality,
            "id": self.constructorId,
            "wiki_url": self.url
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

    def get_full_name(self):
        return self.forename + "  " + self.surname


class Race(Base):
    __tablename__ = 'races'

    raceId = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    circuitId = Column(ForeignKey('circuits.circuitId'), nullable=False)
    name = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)
    time = Column(String(30), nullable=False)
    url = Column(String(30), nullable=False)

    circuit = relationship('Circuit', lazy='joined')

    def to_json(self):
        return {
            "year": self.year,
            "round": self.round,
            "name": self.name,
            "date": self.date,
            "time_of_day": self.time,
            "circuit": self.circuit.to_json()
        }


class Season(Base):
    __tablename__ = 'seasons'

    year = Column(Integer, primary_key=True)
    url = Column(String(30))

    def to_json(self):
        return {
            "year": self.year,
            "wiki_url": self.url
        }


class Status(Base):
    __tablename__ = 'status'

    statusId = Column(Integer)
    status = Column(String(30), primary_key=True)


class ConstructorResult(Base):
    __tablename__ = 'constructor_results'

    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(ForeignKey('races.raceId'), nullable=False)
    constructorId = Column(ForeignKey(
        'constructors.constructorId'), nullable=False)
    points = Column(Integer)
    status = Column(String())

    constructor = relationship('Constructor', lazy='joined')
    race = relationship('Race')

    def to_json(self):
        return {
            "race": self.race.to_json(),
            "team": self.constructor.to_json(),
            "points": self.points,
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
            "team": self.constructor.to_json(),
            "points": self.points,
            "position": self.position,
            "wins": self.wins
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
            "driver": self.driver.to_json(),
            "points": self.points,
            "position": self.position,
            "wins": self.wins,
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
    milliseconds = Column(String(15))

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
            "driver": self.driver.to_json(),
            "team": self.constructor.to_json(),
            "position": self.position,
            "Q1": self.q1 if not self.q1 == "\\N" else None,
            "Q2": self.q2 if not self.q2 == "\\N" else None,
            "Q3": self.q3 if not self.q3 == "\\N" else None,
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
    fastestLapSpeed = Column(String(10))
    statusId = Column(ForeignKey('status.statusId'))

    constructor = relationship('Constructor')
    driver = relationship('Driver')
    race = relationship('Race')
    status = relationship('Status', lazy='joined')

    def to_json(self):
        if self.statusId == 1:
            return {
                "driver": self.driver.to_json(),
                "team": self.constructor.to_json(),
                "grid": self.grid,
                "position": self.position,
                "position_order": self.positionOrder,
                "laps": self.laps,
                "time": self.time,
                "points": self.points,
                "fastest_lap": self.fastestLap,
                "fastest_lap_time": self.fastestLapTime,
                "fastest_lap_speed": self.fastestLapSpeed,
                "status": self.status.status,
            }
        else:
            return {
                "driver": self.driver.to_json(),
                "team": self.constructor.to_json(),
                "grid": self.grid,
                "position": self.position,
                "position_order": self.positionOrder,
                "laps": self.laps,
                "points": self.points,
                "fastest_lap": self.fastestLap,
                "fastest_lap_time": self.fastestLapTime,
                "fastest_lap_speed": self.fastestLapSpeed,
                "status": self.status.status,
            }
