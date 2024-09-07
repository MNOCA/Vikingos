from vikingsClasses import Viking, Saxon, War
import random, sys, io

# Reconfigure stdout to use UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Start variables
viking_names = ['Erik', 'Leif', 'Bjorn', 'Ragnar', 'Ivar', 'Olaf', 'Sigurd', 'Harald', 'Ulf', 'Gunnar']
war = War()
round = 1


# Create army of 10 Vikings
for name in viking_names:
    viking = Viking(name, 100, random.randint(90, 100))
    war.addViking(viking)


# Create army of 10 Saxons
for _ in range(10):
    saxon = Saxon(100, random.randint(90, 100))
    war.addSaxon(saxon)


# Ready message
vikings_ready = f"{', '.join(viking_names[:9])} and {viking_names[9]}"
saxons_ready = f"{', '.join('Saxon' for _ in range(9))} and another Saxon"
print(f"\n⚔️ MIGHTY VIKING ARMY  ✅ => {vikings_ready}")
print(f"🏹 NAMELESS SAXON ARMY ✅ => {saxons_ready}")
print(f"\n🔥🔥🔥🔥🔥🔥  F I G H T !!!  🔥🔥🔥🔥🔥🔥")


# Battle rounds
while war.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
    vikings_count = len(war.vikingArmy)
    saxons_count = len(war.saxonArmy)
    if vikings_count > saxons_count:
        print(f"\nROUND {round} => ⚔️ Vikings are now in the MAJORITY: {vikings_count} > {saxons_count}")
    elif vikings_count < saxons_count:
        print(f"\nROUND {round} => 🏹 Vikings are now OUTNUMBERED: {vikings_count} < {saxons_count}")
    else:
        print(f"\nROUND {round} => ⚖️ The two armies are now EVEN: {vikings_count} = {saxons_count}")
    viking_action = war.vikingAttack()
    if len(war.saxonArmy) == 0:
        print(viking_action)
        break
    else:
        saxon_action = war.saxonAttack()
        print(viking_action, '|', saxon_action)
    round += 1


# Present winner
print()
winner = war.showStatus()
if winner == 'Vikings have won the war of the century!':
    print(f"⚔️⚔️⚔️ {war.vikingArmy[0].battleCry()} ⚔️⚔️⚔️")
print(winner)
