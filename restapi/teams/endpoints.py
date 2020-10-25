from flask import Blueprint

from restapi.teams.controllers import get_team_by_id, get_all_teams

team_bp = Blueprint('team_bp', __name__, url_prefix='/api/teams')

@team_bp.route('/', methods=['GET'])
def get_teams():
    teams = get_all_teams()

    return { "teams" : [team.to_json() for team in teams]}

@team_bp.route('/<id>', methods=['GET'])
def get_team(id=0):
        team = get_team_by_id(id=id)
        if team:
            return team.to_json()
        else:
            return "No team with that id", 400