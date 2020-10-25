from restapi import api, app


@app.route('/', methods=['GET]'])
def index():
    return "Index"


@app.route('/circuits', methods=['GET'])
def circuits():
    circuits = api.get_circuits()
    return {"Circuits": [circuit.to_json() for circuit in circuits]}


@app.route('/races', defaults={'year': '2020'}, methods=['GET'])
@app.route('/races/<year>', methods=['GET'])
def races(year="2020"):
    races = api.get_races_in_year(year)
    return {"Races": [race.to_json() for race in races]}


@app.route('/drivers')
def drivers():
    drivers = api.get_drivers()
    return {"Drivers": [driver.to_json() for driver in drivers]}


@app.route('/results', defaults={"year": "2020", "season_round": "1"}, methods=['GET'])
@app.route('/results/<year>', defaults={"season_round": "0"}, methods=['GET'])
@app.route('/results/<year>/<season_round>', methods=['GET'])
def results(year='2020', season_round='0'):
    if not season_round == '0':
        race = api.get_race(year, season_round)
        if race is None:
            return "Race not found", 400
        response = compile_race_results_report(race)
    else:
        response = {"season_results": []}
        races = api.get_races_in_year(year)
        for race in races:
            race_results = compile_race_results_report(race)
            response["season_results"].append(race_results)
    return response


@app.route('/qualifying', defaults={"year": "2020", "season_round": "1"}, methods=['GET'])
@app.route('/qualifying/<year>', defaults={"season_round": "0"}, methods=['GET'])
@app.route('/qualifying/<year>/<season_round>', methods=['GET'])
def qualifying(year, season_round):
    if not season_round == '0':
        race = api.get_race(year, season_round)
        if race is None:
            return "Race not found", 400
        response = compile_qualifying_results_report(race)
    else:
        races = api.get_races_in_year(year)
        response = {"season_qualifying_results": []}
        for race in races:
            qualifying_results = compile_qualifying_results_report(race)
            response["season_qualifying_results"].append(qualifying_results)

    return response


def compile_race_results_report(race):
    driver_results = api.get_results_from_race(race.raceId, True)
    data = {
        "race": race.to_json(), "results": {
            "driver_results": [], "constructor_results": []
        }
    }
    for result in driver_results:
        data["results"]["driver_results"].append(result.to_json())

    constructor_results = api.get_constructor_results_by_race(race.raceId)
    for result in constructor_results:
        tmp = {"constructor":  result.constructor.to_json(),
               "points": result.points}
        data["results"]["constructor_results"].append(tmp)

    return data


def compile_qualifying_results_report(race):
    qualifying_results = api.get_qualifying_results_by_race(race.raceId)
    data = {"race": race.to_json(), "results": []}

    for result in qualifying_results:
        data["results"].append(result.to_json())

    return data
