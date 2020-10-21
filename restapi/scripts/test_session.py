from restapi import api


if __name__ == "__main__":
    # circuits = api.get_circuits()
    # for circuit in circuits:
    #     print(circuit.name)

    # drivers = api.get_drivers()
    # for driver in drivers:
    #     print(driver.code)
    # race = api.get_race(2020, 1)
    # teams = api.get_teams()
    # if teams:
    #     team_id = teams[0].constructorId
    # if race is not None:
    #     race_id = race.raceId
    #     standings = api.get_constructor_standings_from_race(race_id=race_id, constructor_id=team_id)
    #     print(len(standings))
    #     print(standings[0].to_json())
    # else:
    #     print("Did not find race")

    results = api.get_results_from_race(1032, True)
    print([r.to_json() for  r in results])
    # for race in races:
    #     print(race.to_json())
    # ham = api.get_driver("hamilton")
    # driverId = ham.driverId
    # standings = api.get_driver_standings(driverId)
    # for stand in standings:
    #     print([stand.points, stand.raceId])