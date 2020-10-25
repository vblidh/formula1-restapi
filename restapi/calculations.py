from restapi import api

def get_constr_standings_each_year(constructor_id):
    res = []
    results = api.get_id_of_last_race_of_years()
    race_ids = [r.raceId for r in results]
    res = api.get_constructor_standings_from_races(race_ids, constructor_id)
    res.sort(key=lambda x: x.race.year)

    return res