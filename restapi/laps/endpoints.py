from flask import Blueprint, request
from restapi.laps.controllers import get_laptimes

laptime_bp = Blueprint('lap_blp', __name__, url_prefix='/api/laptimes')


@laptime_bp.route('/<id>', methods=['GET'])
def get_laptimes_of_race(id):

    try:
        race_id = int(id)
    except ValueError:
        return "Race id must be an integer", 400
    laptimes = get_laptimes(race_id)

    resp = {"data": [l.to_json() for l in laptimes]}

    return resp
