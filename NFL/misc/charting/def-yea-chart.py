from statistics import mean
import matplotlib.pyplot as plt

ypra = [4.3,4.9,5,3.5,4.1,5.1,3.8,4.7,5,4.9,5.6,5,5.1,3.1,3.6,3.3,5.4,3.9,3.9,4.2,4.6,5.1,4,5.1,3.7,5,4,2.9,5.1,4.3,4.8,4.4]
yppa = [7.4,7,7.1,5.3,6,6.7,6.1,6.9,4.8,5.3,7.5,6.3,7,6.7,6.7,6,6.6,7,7.5,7.8,7.6,6.5,6.2,6.7,7.3,4.8,6.4,5,8.7,5.6,7.7,7.5]
abb = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAC","KC","LAC","LAR","LV","MIA","MIN","NE","NO","NYG","NYJ","PHI","PIT","SF","SEA","TB","TEN","WAS"]

colors = []
lar = mean(ypra)
lap = mean(yppa)
for i in range(len(ypra)):
    if ypra[i] >= lar and yppa[i] >= lap:
        colors.append('red')
    elif ypra[i] <= lar and yppa[i] <= lap:
        colors.append('green')
    else:
        colors.append('blue')

fig, ax = plt.subplots(figsize=(12,10))
fig.suptitle('Defensive Run/Pass Efficiency thru Week 4 of 2022',fontsize=16)
fig.set_facecolor("white")
ax.scatter(ypra,yppa,color=colors)
ax.set_xlim(min(ypra)-.1,max(ypra)+.1)
ax.set_ylim(min(yppa)-.1,max(yppa)+.1)
ax.set_xlabel("Yards Allowed Per Rush Attempt")
ax.set_ylabel("Yards Allowed Per Pass Attempt")
ax.hlines(lap,min(ypra)-.1,max(ypra)+.1,'orange')
ax.text(lar,max(yppa)+.2,"League Avg RYAPA",ha='center',va='center')
ax.vlines(lar,min(yppa)-.1,max(yppa)+.1,'orange')
ax.text(max(ypra)+.2,lap,"League Avg PYAPA",ha='center',va='center',rotation=270)
for i, team in enumerate(abb):
    ax.annotate(team, (ypra[i],yppa[i]+0.05))
fig.savefig('/Volumes/GoogleDrive/My Drive/def-graph-rp.png')
fig.show()

for i in range(len(yppa)):
    if yppa[i] >= 6.5 and yppa[i] < 7 and ypra[i] > 5 and ypra[i] < 5.25:
        print(abb[i])

for i in range(len(yppa)):
    if yppa[i] == min(yppa):
        print(abb[i])
