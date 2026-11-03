import json 
import random

symbols = ["🍒", "🍋", "⭐", "💎", "🍀"]

COST = 25 

with open("data/player.json", "r") ad f:
  player = json.load(f)

if player["coins"] < COST:
  print("Non hai abbastanza coins!")
  exit()

player["coins"] -= COST

spin = [random.choice(symbols) for_in range(3)]

reward = 0 
if spin[0] == spin[1] == spin[2]:
  reward = 250
  player["jackpots"] += 1
  result = "JACKPOTS"
elif spin[0] == spin[1] == spin[2]:
  reward = 50
  result = "WIN"
else:
  result: "LOSE"

player["coins"] += reward
player["spins"] += 1

player["xp"] += 10

if player["xp"] >= player["level"] * 10
  player["level"] += 1
  player["xp"] = 0 

with open("data/player.json", "w") as f:
  json.dump(player, f, indent=2)

print(spin)
print(result)

with open("REAMDE.md", "w", encoding="utf-8") as f:
  f.write(F"""# 🎰GitHub Casino
  💰 Coins: {player['coins']}
  ⭐ Level: {player['level']}
  🏆 Jackpots: {player['jackpots']}
  🎮 Spin: {player['spin']}

  Ultima giocata:

   {(spin[0] {spin[1]} {spin[2]}

   Risultato:
   {result}
   """)
  
  
  
