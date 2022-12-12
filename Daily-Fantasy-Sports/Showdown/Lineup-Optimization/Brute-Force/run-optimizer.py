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
dset = pd.DataFrame({"player": [], "points": [], "salary": [], "capt. salary": [], "capt. points": []})
for player in players:
    d = arine[arine["player"] == player].sort_values(by = ["salary"],ascending = False).reset_index(drop=True)
    dset.loc[len(dset)] = [player, d["points"][1], d["salary"][1], d["salary"][0], d["points"][0]*1.5]
    

print(f'Chosen Lineup: {pickLineup(dset,budget=50000,num_utility=5)}')
