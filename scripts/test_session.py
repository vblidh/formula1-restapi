from restapi.drivers.calculations import calculate_podiums

if __name__ == "__main__":
    # res = get_constr_standings_each_year(1)
    # team = api.get_team(1)
    # print(team.to_json())
    # for r in res:
    #     print(r.raceId, r.position, r.race.year, r.points)

    res = calculate_podiums(1)
    print(res)