from flask import Blueprint, request
from restapi.drivers.controllers import get_driver, get_driver_by_code, get_drivers
from restapi.drivers.calculations import calculate_podiums, calculate_poles

driver_bp = Blueprint('driver_blp', __name__, url_prefix='/api/drivers')


@driver_bp.route('/', methods=['GET'])
def get():
    code = request.args.get('code')
    res = {}
    if code is not None:
        driver = get_driver_by_code(code)
        if not driver:
            return "No driver exists with that code", 404
        elif len(driver) == 1:
            return driver[0].to_json()
        else:
            return {"Drivers" : [d.to_json() for d in driver]} 
    else:
        drivers = get_drivers()
        res = {"Drivers" : [d.to_json() for d in drivers]}
    return res

@driver_bp.route('/<id>', methods=['GET'])
def retreive(id):
    try:
        driver_id = int(id)
        driver = get_driver(driver_id)
        if driver is None:
            return "No driver with id " + id, 404
        else:
            return driver.to_json()
    except:
        return "Incorrect id, need to enter a number", 400

@driver_bp.route('/podiums/<id>', methods=['GET'])
def get_podiums(id):

    wins, podiums = calculate_podiums(id)

    return {"wins" : wins, "podiums": podiums }

@driver_bp.route('/poles/<id>', methods=['GET'])
def get_poles(id):
    poles = calculate_poles(id)
    return str(poles)

