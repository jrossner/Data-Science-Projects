from pickLineup import pickLineup
import pandas as pd
from os import listdir

print("Reading data file...")
d = pd.read_csv("Daily-Fantasy-Sports/Showdown/Lineup-Optimization/Brute-Force/data/phi:sac.csv")

print("Shaping data...")
raw = pd.DataFrame({"player": d["Name"], "salary": d["Salary"], "points": d["AvgPointsPerGame"]})

print("Filtering out ineligible players...")
out = ["Alex Len","Tyrese Maxey"]
raw = raw[~raw["player"].isin(out)].reset_index(drop=True)

print("Assembling players...")
players = list(raw["player"].unique())
dset = pd.DataFrame({"player": [], "points": [], "salary": [], "capt. salary": [], "capt. points": []})
for player in players:
    d = raw[raw["player"] == player].sort_values(by = ["salary"],ascending = False).reset_index(drop=True)
    dset.loc[len(dset)] = [player, d["points"][1], d["salary"][1], d["salary"][0], d["points"][0]*1.5]

print("Filtering out players below minimnum salary...")
dset = dset[dset["salary"] > 100]

print("Starting optimized picker...")
print(f'Chosen Lineup: {pickLineup(dset,budget=50000,num_utility=5)}')
