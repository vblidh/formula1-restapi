from restapi.drivers.controllers import (
    get_driver, 
    )

from restapi.results.controllers import get_last_results_of_driver, get_all_driver_results, get_all_driver_poles

def calculate_podiums(driver_id):
    results = get_all_driver_results(driver_id)
    podiums = 0
    wins = 0
    for res in results:
        pos = res.position
        if isinstance(pos, int):
            if pos == 1:
                podiums += 1
                wins += 1
            elif pos < 4:
                podiums += 1
            
    return wins, podiums

def calculate_poles(driver_id):
    poles = get_all_driver_poles(driver_id)
    return len(poles)

