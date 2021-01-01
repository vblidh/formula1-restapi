from flask import Blueprint, request
from collections import defaultdict

from restapi.circuits.controllers import get_circuit, get_circuits
from restapi.results.controllers import get_results_from_races
from restapi.races.controllers import get_races_in_circuit

circuit_bp = Blueprint('circuit_endpoints', __name__,
                       url_prefix='/api/circuits')


@circuit_bp.route('/', defaults={'id': '0'}, methods=['GET'])
@circuit_bp.route('/<id>/', methods=['GET'])
def index(id):
    if id == '0':
        circuits = get_circuits()
        return {"circuits": [c.to_json() for c in circuits]}
    else:
        try:
            circuit_id = int(id)
            res = get_circuit(circuit_id)
            if res:
                return res.to_json()
            else:
                return "No circuit with id " + id, 404
        except ValueError:
            return "Invalid circuit, need an integer", 400


@circuit_bp.route('/<id>/results/', methods=['GET'])
def get_results(id):
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        include_upcoming = bool(int(request.args.get('include_upcoming', 0)))

    except ValueError:
        return "Invalid page/page_size", 400
    start = (page-1)*page_size
    end = start + page_size
    print(include_upcoming)
    count, races = get_races_in_circuit(
        id, start, end, include_upcoming=include_upcoming)
    race_ids = [r.raceId for r in races]
    results = get_results_from_races(race_ids=race_ids, order_by="date")
    data = defaultdict(lambda: defaultdict(list))
    for res in results:
        data[res.race.year]["race_id"] = res.race.raceId
        data[res.race.year]["results"].append(res.to_json())
    resp = {"data": data, "total_entries": count}
    # print(len(resp.get('data')))
    return resp
