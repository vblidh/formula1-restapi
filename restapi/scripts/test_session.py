from restapi import api
from restapi.calculations import get_constr_standings_each_year

if __name__ == "__main__":
    res = get_constr_standings_each_year(1)
    team = api.get_team(1)
    print(team.to_json())
    for r in res:
        print(r.raceId, r.position, r.race.year, r.points)