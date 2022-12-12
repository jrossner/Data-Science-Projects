from pickLineup import pickLineup
import pandas as pd
from os import listdir

print(f'directories: {listdir()}')

d = pd.read_csv("Daily-Fantasy-Sports/Showdown/Lineup-Optimization/Brute-Force/data/DKSalaries.csv")

arine = pd.DataFrame({"player": d["Name"], "salary": d["Salary"], "points": d["AvgPointsPerGame"]})
out = ["Rondale Moore","Jakobi Meyers","Brian Hoyer", "Quinn Nordin","Bailey Zappe"]
arine = arine[~arine["player"].isin(out)].reset_index(drop=True)
arine_clean = arine[arine["salary"] > 2000]

players = list(arine["player"].unique())
dset = pd.DataFrame({"player": [], "salary": [], "points": [], "capt. salary": [], "capt. points": []})
for player in players:
    d = arine[arine["player"] == player].sort_values(by = ["salary"],ascending = False).reset_index(drop=True)
    dset = dset.append({"player": player, "points": d["points"][1], "salary": d["salary"][1],
                        "capt. salary": d["salary"][0], "capt. points": d["points"][0]*1.5},ignore_index=True)

print(f'Chosen Lineup: {pickLineup(dset,budget=50000,num_utility=5)}')
