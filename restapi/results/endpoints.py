from flask import Blueprint, request

from restapi.results.controllers import (
    get_results_from_race,
    get_results_from_races,
    get_team_result,
    get_qualifying_results,
    get_last_results_of_driver
)
from restapi.races.controllers import get_race, get_races_in_year, get_last_race, get_race_by_id
from restapi.drivers.controllers import get_driver


result_bp = Blueprint('result_bp', __name__, url_prefix='/api/results')


@result_bp.route('/race', methods=['GET'])
def get_result():
    resp = {"data": []}
    year = request.args.get('year')
    if year:
        try:
            year = int(year)
            race_number = request.args.get('round')
            if race_number:
                race_number = int(race_number)
                races = [get_race(year, race_number)]
                res = get_results_from_race(race_id=races[0].raceId)
            else:
                races = get_races_in_year(year)
                race_ids = [r.raceId for r in races]
                res = get_results_from_races(race_ids=race_ids)

        except ValueError:
            return "Invalid year/round, must be numbers", 400
    else:
        races = [get_last_race()]
        res = get_results_from_race(races[0].raceId)

    races.reverse()
    for race in races:
        tmp = {"race": race.to_json()}
        race_results = list(filter(lambda x: x.raceId == race.raceId, res))
        if race_results:
            tmp["results"] = [r.to_json() for r in race_results]
            resp["data"].append(tmp)
    return resp


@result_bp.route('/qualifying', methods=['GET'])
def get_qualifying():
    resp = {"data": []}
    year = request.args.get('year')
    if year:
        try:
            year = int(year)
            qualy_round = request.args.get('round')
            if qualy_round:
                qualy_round = int(qualy_round)
                races = [get_race(year=year, round=qualy_round)]
                res = get_qualifying_results(races[0].raceId)
            else:
                races = get_races_in_year(year)
                race_ids = [r.raceId for r in races]
                res = get_qualifying_results(race_ids)

        except ValueError:
            return "Invalid year/round, must be numbers", 400
    else:
        return "No year specified in query param", 400

    races.reverse()
    for race in races:
        tmp = {"race": race.to_json(), "results": []}
        quali_results = list(filter(lambda x: x.raceId == race.raceId, res))
        if quali_results:
            tmp["results"] = [qr.to_json() for qr in quali_results]
            resp["data"].append(tmp)

    return resp


@result_bp.route("/race/<id>", methods=['GET'])
def retrieve(id):
    try:
        id = int(id)
    except ValueError:
        return "Incorrect race id", 400
    race = get_race_by_id(id)
    if race:
        res = get_results_from_race(id)
        resp = {"data": {}}
        resp["data"]["race"] = race.to_json()
        resp["data"]["results"] = [r.to_json() for r in res]
        return resp
    else:
        return "Race not found", 404
