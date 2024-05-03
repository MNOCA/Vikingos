import tkinter as tk
import random
import time
import vikingsClasses as vc

vikingNames = ["Arne", "Birger", "Bjørn", "Bo", "Erik", "Frode",
                "Gorm", "Halfdan", "Harald", "Knud", "Kåre", "Leif",
                "Njal", "Roar", "Rune", "Sten", "Skarde", "Sune", "Svend",
                "Troels", "Toke", "Torsten", "Trygve", "Ulf", "Ødger", "Åge"]

saxonNames = ["Abba", "Abbi", "Abbilin", "Abbo", "Abger", "Abo", "Abuko",
              "Abulo", "Adala", "Adalbarn", "Adalbold", "Adalbraht",
              "Adalbrand", "Adaldei", "Adalger", "Adalhard", "Adalmar",
              "Adalmund", "Adalold", "Adalric", "Adalward", "Adalwi",
              "Adbraht", "Addi", "Adiko", "Adiman", "Ado", "Adward",
              "Adwig", "Agga", "Aia", "Aico", "Aio", "Aitet", "Akko",
              "Alager", "Alaka", "Alako", "Alaward", "Albern", "Albgot",
              "Albrad", "Albric", "Albrun", "Albwin", "Alda", "Aldako",
              "Aldbert", "Aldbraht", "Aldburg", "Alderd", "Aldfrid",
              "Aldger", "Aldgoð", "Aldiko", "Aldmar", "Aldmund", "Aldolf",
              "Aldward", "Athalgard", "Athalgis", "Athalheri", "Athalond",
              "Avi", "Avin", "Avo", "Avuko", "Avutet", "Irmin", "Radolf",
              "Ruma", "Thunerulf"]

class SaxonFighter(vc.Saxon):
    def __init__(self, name, health, strength):
        super().__init__(health=health, strength=strength)
        self.name = name

    def battleCry(self) -> str:
        # for saxon in self.saxonArmy:
            # saxon.health += 1
        return random.choice(["Schlachtet sie!", "Godamite!", "Olicrosse!"])
    

class VikingFighter(vc.Viking):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)

    def battleCry(self) -> str:
        # for viking in self.vikingArmy:
            # viking.health += 1
        return "Odin Owns You All!"


class Battle():
    def __init__(self) -> None:
        self.vikingArmy = []
        self.saxonArmy = []
        self.attackers = random.uniform(1, 100) % 2

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self) -> str:
        # your code here
        attackingViking: vc.Viking = random.choice(self.vikingArmy)
        defendingSaxon: SaxonFighter = random.choice(self.saxonArmy)
        actionBox.insert("end",f"The Viking {attackingViking.name} (S:{attackingViking.strength}) attacked {defendingSaxon.name} (H:{defendingSaxon.health})\n")
        fight_result = defendingSaxon.receiveDamage(attackingViking.strength)
        if "died" in fight_result:
            actionBox.insert("end", f"The viking {defendingSaxon.name} died in battle\n")
            saxons.delete(self.saxonArmy.index(defendingSaxon))
            self.saxonArmy.remove(defendingSaxon)
            for viking in self.vikingArmy:
                viking.battleCry()
        return fight_result

    def saxonAttack(self) -> str:
        # your code here
        attackingSaxon: SaxonFighter = random.choice(self.saxonArmy)
        defendingViking: vc.Viking = random.choice(self.vikingArmy)
        actionBox.insert("end",f"The Saxon {attackingSaxon.name} (S:{attackingSaxon.strength}) attacked {defendingViking.name} (H:{defendingViking.health})\n")
        fight_result = defendingViking.receiveDamage(attackingSaxon.strength)
        if "died" in fight_result:
            actionBox.insert("end", f"The viking {defendingViking.name} died in battle\n")
            vikings.delete(self.vikingArmy.index(defendingViking))
            self.vikingArmy.remove(defendingViking)
            for saxon in self.saxonArmy:
                saxon.battleCry()
        return fight_result

    def showStatus(self) -> str:
        # your code here
        m = ""
        if len(self.saxonArmy) == 0:
            m = "Vikings have won the war of the century!\n"
        elif len(self.vikingArmy) == 0:
            m = "Saxons have fought for their lives and survived another day...\n"
        else:
            m = "Vikings and Saxons are still in the thick of battle.\n"
        return m

def onNewGame():
    
    for _ in range(0, 15):
        viking = vc.Viking(random.choice(vikingNames),
                           random.randint(80, 100),
                           random.randint(80, 100))
        battle.addViking(viking)
        vikings.insert("end", viking.name)

    for _ in range(0, 15):
        saxon = SaxonFighter(random.choice(saxonNames),
                            random.randint(80, 100),
                            random.randint(80, 100))
        battle.addSaxon(saxon)
        saxons.insert("end", saxon.name)

    newGameButton.destroy()
    onNewRound.__setattr__("state", tk.ACTIVE)
    #print("\n",battle.showStatus())

def onNewRound():
    actionBox.insert("end", "\n======= New round =======\n")
    actionBox.insert("end", f"{len(battle.vikingArmy)} viking(s) are fighting {len(battle.saxonArmy)} saxon(s)\n")
    if battle.attackers == 0:
        #print("The Vikings are attacking!")
        actionBox.insert("end", "The Vikings are attacking!\n")
        battle.vikingAttack()
        battle.attackers = 1
    else:
        # print("The Saxons are attacking!")
        actionBox.insert("end", "The Saxons are attacking!\n")
        battle.saxonAttack()
        battle.attackers = 0

    if len(battle.saxonArmy)==0:
        actionBox.insert("end", "======= ! Victory ! =======\n")
        actionBox.insert("end", "Vikings have won the war of the century!\n")
        newRoundButton.destroy()
    elif len(battle.vikingArmy)==0:
        actionBox.insert("end", "======= ! Victory ! =======\n")
        actionBox.insert("end", "Saxons have fought for their lives and survived another day...\n")
        newRoundButton.destroy()
    actionBox.yview_scroll(7, 'units')

app = tk.Tk()
app.title = "WarGame"
app.geometry("400x300")

newGameButton = tk.Button(app, text="New Game", command=onNewGame)
newGameButton.pack()
newGameButton.place(x=230, y=5)

vLabel = tk.Label(app, text="Vikings")
vLabel.pack()
vLabel.place(x=10, y=0)
vikings = tk.Listbox(app, width=10, height=20)
vikings.pack()
vikings.place(x=10, y=30)

sLabel = tk.Label(app, text="Saxons")
sLabel.pack()
sLabel.place(x=120, y=0)
saxons = tk.Listbox(app, width=10, height=20)
saxons.pack()
saxons.place(x=120, y=30)

actionBox = tk.Text(app, width=90, height=25)
actionBox.pack()
actionBox.place(x=230, y=30)

battle = Battle()

newRoundButton = tk.Button(app, text="New Round", command=onNewRound)
onNewRound.__setattr__("state", tk.DISABLED)
newRoundButton.pack()
newRoundButton.place(x=330, y=5)

app.mainloop()
