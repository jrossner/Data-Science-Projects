d = pd.read_csv("/Users/rossner/Downloads/DKSalaries.csv")
arine = pd.DataFrame({"player": d["Name"], "salary": d["Salary"], "points": d["AvgPointsPerGame"]})
arine["capt. points"] = [ p * 1.5 for p in arine["points"]]
arine["capt. salary"] = [ s * 1.5 for s in arine["salary"]]

print(pickLineup(arine,budget=50000,num_utility=5))
