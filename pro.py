from random import choice
players=[]
file=open("player.txt","r")
players=file.read().splitlines()
print(players)
teamA=[]
teamB=[]
while len(players)>0:
  playerA=choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  
  if players==[]:
    break

  playerB=choice(players)
  teamB.append(playerB)
  players.remove(playerB)

print("Team A:",teamA)
print("Team B:",teamB)
