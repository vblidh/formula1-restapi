from flask import Blueprint, request

from restapi.standings.controllers import (
    get_driver_standings_by_race,
    get_driver_standings_by_races,
    get_current_driver_standings,
    get_individual_standing,
    get_constructor_standings_from_race,
    get_constructor_standings_from_races,
)

from restapi.races.controllers import (
    get_races_in_year,
    get_race,
    get_last_race_of_years,
)
from restapi.teams.controllers import get_team_of_driver_in_races


standings_bp = Blueprint('standings_bp', __name__, url_prefix='/api/standings')


@standings_bp.route('/drivers', methods=['GET'])
def get_driver_standings():
    resp = {"driver_standings" : []}
    year = request.args.get('year')
    if year:
        try:
            year = int(year)
            _round = request.args.get('round')
            if _round:
                _round = int(_round)
                races = [get_race(year, _round)]
                if races:
                    res = get_driver_standings_by_race(races[0].raceId)
                else:
                    return "Race not found", 404
            else:
                races = get_races_in_year(year)
                race_ids = [r.raceId for r in races]
                res = get_driver_standings_by_races(race_ids=race_ids)
        
        except ValueError:
            return "Invalid year/round", 400
    else:
        return "Must supply at least a year in query param to get standings", 400
        
    races.reverse()
    for race in races:
        tmp = {"race" : race.to_json()}
        race_standings = list(filter(lambda x: x.raceId == race.raceId, res))
        tmp["standings"] = [s.to_json() for s in race_standings]
        resp["driver_standings"].append(tmp)

    return resp


@standings_bp.route('/drivers/<id>', methods=['GET'])
def retreive_driver_standings(id):
    races = get_last_race_of_years()
    race_ids = [r.raceId for r in races]
    standings = get_driver_standings_by_races(race_ids, id)
    teams =  get_team_of_driver_in_races(id, race_ids)
    data = []
    for s,t in zip(standings, teams):
        tmp = s.to_json2()
        tmp['team'] = t.to_json()
        data.append(tmp)
    resp = {"data": data}
    return resp



@standings_bp.route('/teams', methods=['GET'])
def get_constructor_standings():
    resp = {"team_standings" : []}
    year = request.args.get('year')
    if year:
        try:
            year = int(year)
            _round = request.args.get('round')
            if _round:
                _round = int(_round)
                races = [get_race(year, _round)]
                res = get_constructor_standings_from_race(races[0].raceId)
            else:
                races = get_races_in_year(year)
                race_ids = [r.raceId for r in races]
                res = get_constructor_standings_from_races(race_ids=race_ids)

        except ValueError:
            return "Invalid route param, either supply a number or the string 'latest'", 400
    else:
        return "Must supply at least a year in query param to get standings", 400
    
    races.reverse()
    for race in races:
        tmp = {"race" : race.to_json()}
        race_standings = list(filter(lambda x: x.raceId == race.raceId, res))
        if race_standings:
            tmp["standings"] = [s.to_json() for s in race_standings]
            resp["team_standings"].append(tmp)
    
    return resp