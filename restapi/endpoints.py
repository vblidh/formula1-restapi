from restapi import api, app


@app.route('/', methods=['GET'])
def index():
    circuits = api.get_circuits()
    return {"Circuits" : [circuit.to_json() for circuit in circuits]}