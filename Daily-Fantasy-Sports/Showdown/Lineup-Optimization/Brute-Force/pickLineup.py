import pandas as pd
from itertools import combinations as comb

def pickLineup(data, budget = 50000, num_utility = 5):
    best_lineups = [{"players": [], "total": 0, "salary": 0, "captain": None}]
    data = data.sort_values(by=["points"],ascending=False).reset_index(drop=True)

    for i in range(len(data)):
        capt = data["player"][i]
        c_salary = data["capt. salary"][i]
        c_points = data["capt. points"][i]
        remaining = budget - data["capt. salary"][i]

        rems = data.drop([i]).reset_index(drop=True)
        utility_lineups = list(comb(rems["player"], num_utility))

        for lineup in utility_lineups:
            lineup = list(lineup)
            lineup_data = rems[rems["player"].isin(lineup)]
            if c_salary + sum(lineup_data["salary"]) <= remaining:
                if c_points + sum(lineup_data["points"]) > best_lineups[-1]["total"]:
                    lineup_total = c_points + sum(lineup_data["points"])
                    lineup_salary = c_salary + sum(lineup_data["salary"])
                    best_lineups.append({"players": [capt]+list(lineup_data["player"]),
                                         "total": lineup_total, "salary": lineup_salary,
                                         "captain": capt})

    #best_lineups = sorted(best_lineups, key=lambda d: d['total'], reverse=True)[0:5]

    return best_lineups
