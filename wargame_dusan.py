from vikingsClasses import Soldier, Viking, Saxon, War
import random

vikingNames = ["Kerem", "Julia", "Caroline", "Saul", "Joao" , "Carlos", "Dani", "Tiago"]
war = War()

# Adding the Viking

for i in range(0,8):
        viking = Viking(vikingNames[i],random.randint(1,100),random.randint(1,20))
        war.addViking(viking)
        print(f"{viking.name} has been added to the game with {viking.health} Health and {viking.strength} Strength")
       

          
#Adding the saxons

for i in range(1,8):
    saxon = Saxon(random.randint(1,100),random.randint(1,20))
    war.addSaxon(saxon)
    print(f"Saxon Number {i} has been added to the game wirh {saxon.health} Health and {saxon.strength} Strength")

#Starting the Game
round_of_war = 0
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"Round Number {round_of_war}. Number of remaining Vikings {len(war.vikingArmy)} vs. Number of remaining Saxons {len(war.saxonArmy)}")
    war.showStatus()
    round_of_war += 1

#Final Status of the War

print(war.showStatus())


