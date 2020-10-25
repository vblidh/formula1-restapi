from restapi.db import session

from restapi.models import Constructor

def get_team_by_id(id):
    return session.query(Constructor).filter(Constructor.constructorId == id).one_or_none()


def get_all_teams():
    return session.query(Constructor).all()



