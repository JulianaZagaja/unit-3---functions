#Q1
#Output: [23]

#Q2
#NEXUS

#Q3
def match_mvp(players):
    bestplayer = ""
    bestkd = 0
    for key, value in players.items():
        kd = value["kills"] / value["deaths"]
        if kd > bestkd:
            bestkd = kd
            bestplayer = key
        return bestplayer

players = {
    "pheonix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18}
}

print(match_mvp(players))