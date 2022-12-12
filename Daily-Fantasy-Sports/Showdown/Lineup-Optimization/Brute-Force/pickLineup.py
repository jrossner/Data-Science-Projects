import pandas as pd
from itertools import combinations as comb

def pickLineup(data, budget = 50000, num_utility = 5):
    best_lineup = {"players": [], "total": 0, "salary": 0, "captain": None}
    data = data.sort_values(by=["points"],ascending=False).reset_index()

    for i in range(len(data)):
        capt = data["player"][i]
        c_salary = data["capt. salary"][i]
        c_points = data["capt. points"][i]
        remaining = budget - data["capt. salary"][i]

        rems = data.drop([i]).reset_index()
        utility_lineups = list(comb(rems["player"], num_utility))
        
        for lineup in utility_lineups:
            lineup = list(lineup)
            lineup_data = rems[rems["player"].isin(lineup)]
            if c_salary + sum(lineup_data["salary"]) <= remaining:
                if c_points + sum(lineup_data["points"]) > best_lineup["total"]:
                    lineup_total = c_points + sum(lineup_data["points"])
                    lineup_salary = c_salary + sum(lineup_data["salary"])
                    print("found a better line up")
                    best_lineup = {"players": [capt]+list(lineup_data["player"]),
                                    "total": lineup_total, "salary": lineup_salary,
                                    "captain": capt}
            
    return best_lineup
