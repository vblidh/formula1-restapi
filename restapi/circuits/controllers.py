from restapi.db import session
from restapi.models import Circuit


def get_circuits():
    circuits = session.query(Circuit).all()
    return circuits


def get_circuit(id):
    return session.query(Circuit).filter(Circuit.circuitId == id).one_or_none()
