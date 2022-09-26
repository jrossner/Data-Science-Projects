import matplotlib.pyplot as plt
from statistics import mean

rypa = [4.5,4.9,5.6,4.7,4.7,5.4,3.3,5,4,4.2,5.9,4.7,3.6,4,4.1,4.1,2.6,3.4,4.5,3.3,4.9,4.3,5.5,5.2,4.4,4.4,4.1,4.5,4,3.4,3.5,3.7]
pypa = [5.5,8.1,8.5,7.6,6.8,6.6,6.5,6.5,5.9,7,6.7,7.6,6.2,6.6,7,7.8,7.2,7.5,7.1,9,6.4,8.1,7.5,6.6,5.9,9.3,5.5,6.9,7,6.5,7.8,6.6]
abb = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAC","KC","LV","LAC","LAR","MIA","MIN","NE","NO","NYG","NYJ","PHI","PIT","SF","SEA","TB","TEN","WAS"]

fig, ax = plt.subplots(figsize=(12,10))
fig.suptitle('NFL Teams Offensive Efficiency thru Sunday of Week 3 of 2022',fontsize=16)
fig.set_facecolor("white")
ax.scatter(rypa,pypa)
ax.set_xlim(2.5,6.2)
ax.set_ylim(5.25,9.5)
ax.set_xlabel("Rushing Yards per Attempt")
ax.set_ylabel("Passing Yards per Attempt")
ax.hlines(mean(pypa),2.5,6.2,'red')
ax.text(mean(rypa),9.6,"League Average Rush Y/A",ha='center',va='center')
ax.vlines(mean(rypa),5.25,9.5,'red')
ax.text(6.3,mean(pypa),"League Average Pass Y/A",ha='center',va='center',rotation=270)
for i, team in enumerate(abb):
    ax.annotate(team, (rypa[i],pypa[i]+0.075))
fig.savefig('/Volumes/GoogleDrive/My Drive/a.png')
fig.show()
