from flask import Blueprint, request
import time
from restapi.races.controllers import (
    get_race, 
    get_all_races,
    get_races_in_year,
    get_id_of_last_race_of_years,
)


race_bp = Blueprint('race_blp', __name__, url_prefix='/api/races')


@race_bp.route('/', methods=['GET'])
def get_races():
    year = request.args.get('year')
    season_round = request.args.get('round')
    data = {"Races" : []}
    try:
        if year:
            year = int(year)    
            if season_round:
                season_round = int(season_round)
                race = get_race(year, season_round)
                data["Races"].append(race.to_json())
            else:
                races = get_races_in_year(year)
                data["Races"] = [r.to_json() for r in races]
        else:
            races = get_all_races()
            before = time.time()
            races.sort(key=lambda x: x.date)
            print("Sort time: %s seconds:", (time.time() - before))
            data["Races"] = [r.to_json() for r in races]
        return data
    except ValueError as err:
        print(err)
        return "Invalid query parameter", 400

