DROP TABLE IF EXISTS "constructors";
CREATE TABLE IF NOT EXISTS "constructors" (
	"constructorId"	INTEGER NOT NULL,
	"constructorRef"	TEXT NOT NULL,
	"name"	TEXT NOT NULL UNIQUE,
	"nationality"	TEXT,
	"url"	TEXT NOT NULL,
	UNIQUE("name"),
	PRIMARY KEY("constructorId")
);
DROP TABLE IF EXISTS "status";
CREATE TABLE IF NOT EXISTS "status" (
	"statusId"	INTEGER,
	"status"	,
	PRIMARY KEY("statusId")
);
DROP TABLE IF EXISTS "races";
CREATE TABLE IF NOT EXISTS "races" (
	"raceId"	INTEGER NOT NULL,
	"year"	INTEGER NOT NULL,
	"round"	INTEGER NOT NULL,
	"circuitId"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"url"	TEXT NOT NULL,
	PRIMARY KEY("raceId")
);
DROP TABLE IF EXISTS "circuits";
CREATE TABLE IF NOT EXISTS "circuits" (
	"circuitId"	INTEGER,
	"circuitRef"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"location"	TEXT NOT NULL,
	"country"	TEXT NOT NULL,
	"lat"	TEXT,
	"lng"	TEXT,
	"alt"	TEXT,
	"url"	TEXT,
	PRIMARY KEY("circuitId")
);
DROP TABLE IF EXISTS "constructorresults";
CREATE TABLE IF NOT EXISTS "constructorresults" (
	"constructorResultsId"	INTEGER,
	"raceId"	INTEGER NOT NULL,
	"constructorId"	INTEGER NOT NULL,
	"points"	INTEGER,
	"status"	,
	FOREIGN KEY("constructorId") REFERENCES "constructors"("constructorId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	PRIMARY KEY("constructorResultsId")
);
DROP TABLE IF EXISTS "constructorstandings";
CREATE TABLE IF NOT EXISTS "constructorstandings" (
	"constructorStandingsId"	INTEGER,
	"raceId"	INTEGER NOT NULL,
	"constructorId"	INTEGER NOT NULL,
	"points"	INTEGER NOT NULL,
	"position"	INTEGER NOT NULL,
	"positionText"	TEXT,
	"wins"	INTEGER NOT NULL,
	FOREIGN KEY("constructorId") REFERENCES "constructors"("constructorId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	PRIMARY KEY("constructorStandingsId")
);
DROP TABLE IF EXISTS "driverstandings";
CREATE TABLE IF NOT EXISTS "driverstandings" (
	"driverStandingsId"	INTEGER,
	"raceId"	INTEGER NOT NULL,
	"driverId"	INTEGER NOT NULL,
	"points"	INTEGER,
	"position"	INTEGER,
	"positionText"	TEXT,
	"wins"	INTEGER,
	FOREIGN KEY("driverId") REFERENCES "drivers"("driverId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	PRIMARY KEY("driverStandingsId")
);
DROP TABLE IF EXISTS "drivers";
CREATE TABLE IF NOT EXISTS "drivers" (
	"driverId"	INTEGER,
	"driverRef"	TEXT NOT NULL,
	"number"	INTEGER NOT NULL,
	"code"	TEXT,
	"forename"	TEXT,
	"surname"	TEXT,
	"dob"	TEXT,
	"nationality"	TEXT,
	"url"	TEXT,
	PRIMARY KEY("driverId")
);
DROP TABLE IF EXISTS "laptimes";
CREATE TABLE IF NOT EXISTS "laptimes" (
	"raceId"	INTEGER,
	"driverId"	INTEGER,
	"lap"	INTEGER,
	"position"	INTEGER,
	"time"	TEXT,
	"milliseconds"	TEXT,
	FOREIGN KEY("driverId") REFERENCES "drivers"("driverId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	PRIMARY KEY("raceId","driverId","lap")
);
DROP TABLE IF EXISTS "pitstops";
CREATE TABLE IF NOT EXISTS "pitstops" (
	"raceId"	INTEGER,
	"driverId"	INTEGER,
	"stop"	INTEGER,
	"lap"	INTEGER NOT NULL,
	"time"	TEXT NOT NULL,
	"duration"	TEXT NOT NULL,
	"milliseconds"	TEXT,
	FOREIGN KEY("driverId") REFERENCES "drivers"("driverId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	PRIMARY KEY("raceId","driverId","stop")
);
DROP TABLE IF EXISTS "qualifying";
CREATE TABLE IF NOT EXISTS "qualifying" (
	"qualifyId"	INTEGER,
	"raceId"	INTEGER,
	"driverId"	INTEGER,
	"constructorId"	INTEGER,
	"number"	INTEGER,
	"position"	INTEGER NOT NULL,
	"q1"	TEXT,
	"q2"	TEXT,
	"q3"	TEXT,
	FOREIGN KEY("driverId") REFERENCES "drivers"("driverId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	FOREIGN KEY("constructorId") REFERENCES "constructors"("constructorId"),
	PRIMARY KEY("qualifyId")
);
DROP TABLE IF EXISTS "seasons";
CREATE TABLE IF NOT EXISTS "seasons" (
	"year"	INTEGER,
	"url"	TEXT,
	PRIMARY KEY("year")
);
DROP TABLE IF EXISTS "results";
CREATE TABLE IF NOT EXISTS "results" (
	"resultId"	INTEGER,
	"raceId"	INTEGER,
	"driverId"	INTEGER,
	"constructorId"	INTEGER,
	"number"	INTEGER,
	"grid"	INTEGER,
	"position"	INTEGER,
	"positionText"	TEXT,
	"positionOrder"	NUMERIC,
	"points"	INTEGER,
	"laps"	INTEGER,
	"time"	TEXT,
	"milliseconds"	INTEGER,
	"fastestLap"	INTEGER,
	"rank"	INTEGER,
	"fastestLapTime"	TEXT,
	"fastestLapSpeed"	TEXT,
	"statusId"	INTEGER,
	FOREIGN KEY("statusId") REFERENCES "status"("statusId"),
	FOREIGN KEY("raceId") REFERENCES "races"("raceId"),
	FOREIGN KEY("driverId") REFERENCES "drivers"("driverId"),
	FOREIGN KEY("constructorId") REFERENCES "constructors"("constructorId"),
	PRIMARY KEY("resultId")
);
