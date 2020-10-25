from flask import Blueprint
from restapi.circuits.controllers import get_circuit, get_circuits

circuit_bp = Blueprint('circuit_endpoints', __name__,url_prefix='/api/circuits')


@circuit_bp.route('/',defaults={'id': '0'}, methods=['GET'])
@circuit_bp.route('/<id>/', methods=['GET'])
def index(id):
    if id=='0':
        res = get_circuits()
        return {"Circuits": [c.to_json() for c in res]}
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