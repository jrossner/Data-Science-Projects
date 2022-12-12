from pickLineup import pickLineup
import pandas as pd
from os import listdir

print(f'directories: {listdir()}')

d = pd.read_csv("Daily-Fantasy-Sports/Showdown/Lineup-Optimization/Brute-Force/data/DKSalaries.csv")

arine = pd.DataFrame({"player": d["Name"], "capt. salary": d["Salary"], "points": d["AvgPointsPerGame"]})
arine["capt. points"] = [ p * 1.5 for p in arine["points"]]
arine["salary"] = [ s / 1.5 for s in arine["capt. salary"]]

out = ["Rondale Moore","Jakobi Meyers","Brian Hoyer", "Quinn Nordin"]
arine = arine[~arine["player"].isin(out)].reset_index(drop=True)
arine_clean = arine[arine["salary"] > 2000]

print(f'Chosen Lineup: {pickLineup(arine_clean,budget=50000,num_utility=5)}')
