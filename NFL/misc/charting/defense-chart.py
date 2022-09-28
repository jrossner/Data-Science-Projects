ypp = [6.7,6,6.5,4.1,5,5.7,4.8,5.6,4.8,4.7,5.8,5.6,5.7,4.8,5.2,4.6,5.7,5.3,5.7,6.3,6,5.4,5,5.9,5.5,4.5,5.1,3.9,6.3,4.5,6.4,6.3]
ppp = [0.503,0.429,0.365,0.241,0.284,0.3,0.281,0.419,0.265,0.225,0.441,0.28,0.272,0.313,0.216,0.316,0.454,0.359,0.389,0.323,0.268,0.403,0.349,0.337,0.44,0.251,0.286,0.214,0.372,0.141,0.447,0.429]
abb = ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAC","KC","LV","LAC","LAR","MIA","MIN","NE","NO","NYG","NYJ","PHI","PIT","SF","SEA","TB","TEN","WAS"]

colors = []
lay = mean(ypp)
lap = mean(ppp)
for i in range(len(rypa)):
    if ypp[i] >= lay and ppp[i] >= lap:
        colors.append('red')
    elif ypp[i] <= lay and ppp[i] <= lap:
        colors.append('green')
    else:
        colors.append('blue')

fig, ax = plt.subplots(figsize=(12,10))
fig.suptitle('NFL Teams Defensive Effectiveness thru Week 3 of 2022',fontsize=16)
fig.set_facecolor("white")
ax.scatter(ypp,ppp,color=colors)
ax.set_xlim(min(ypp)-.07,max(ypp)+.07)
ax.set_ylim(min(ppp)-.025,max(ppp)+.025)
ax.set_xlabel("Yards Allowed Per Play")
ax.set_ylabel("Points Allowed Per Play")
ax.hlines(lap,min(ypp)-.07,max(ypp)+.07,'orange')
ax.text(lay,max(ppp)+.035,"League Avg YAPP",ha='center',va='center')
ax.vlines(lay,min(ppp)-.025,max(ppp)+.025,'orange')
ax.text(max(ypp)+.1,lap,"League Avg PAPP",ha='center',va='center',rotation=270)
for i, team in enumerate(abb):
    ax.annotate(team, (ypp[i],ppp[i]+0.005))
fig.savefig('/Volumes/GoogleDrive/My Drive/def-graph.png')
fig.show()
