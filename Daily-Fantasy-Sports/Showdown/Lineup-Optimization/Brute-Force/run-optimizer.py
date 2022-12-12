from pickLineup import pickLineup
import pandas as pd
from os import listdir

print(f'directories: {listdir('')}')

d = pd.read_csv("Daily-Fantasy-Sports/Showdown/Lineup-Optimization/Brute-Force/data/DKSalaries.csv")

arine = pd.DataFrame({"player": d["Name"], "salary": d["Salary"], "points": d["AvgPointsPerGame"]})
arine["capt. points"] = [ p * 1.5 for p in arine["points"]]
arine["capt. salary"] = [ s * 1.5 for s in arine["salary"]]
arine_2000 = arine[arine["salary"] > 1900]

print(f'Chosen Lineup: {pickLineup(arine_2000,budget=50000,num_utility=5)}')
