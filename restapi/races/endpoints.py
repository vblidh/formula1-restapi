from flask import Blueprint, request
import time
from restapi.races.controllers import (
    get_last_race, get_race, 
    get_all_races,
    get_races_in_year,
    get_last_race_of_years,
)



race_bp = Blueprint('race_blp', __name__, url_prefix='/api/races')


@race_bp.route('/', methods=['GET'])
def get_races():
    year = request.args.get('year')
    season_round = request.args.get('round')
    data = {}
    try:
        if year:
            year = int(year)    
            if season_round:
                season_round = int(season_round)
                race = get_race(year, season_round)
                data["races"] = [race.to_json()]
            else:
                races = get_races_in_year(year)
                data["races"] = [r.to_json() for r in races]
        else:
            races = get_all_races()
            before = time.time()
            races.sort(key=lambda x: x.date)
            data["races"] = [r.to_json() for r in races]
        return data
    except ValueError as err:
        print(err)
        return "Invalid query parameter", 400

@race_bp.route('/rounds', methods=['GET'])
def get_race_amount():
    year = request.args.get('year')
    if year == "latest":
        race = get_last_race()
        return str(race.round)
    elif year:
        try:
            year = int(year)
            race = get_last_race_of_years(year);
            if race:
                print(race)
                return str(race.round);
            else:
                return "Must enter a year between 1950 and 2020", 400
        except ValueError:
            return "Incorrect year, must be a number", 400
    else:
        return "Must supply a year in query param, i.e ?year=xxxx", 400