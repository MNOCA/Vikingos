import random
import tkinter as tk
from vikingsClasses import Soldier, Viking, Saxon, War

# Viking Names List
vikingNames = ["Kerem", "Julia", "Caroline", "Saul", "Joao", "Carlos", "Dani", "Tiago"]

# Initialize War
war = War()

# Main Window
root = tk.Tk()
root.title("Wargames")

root.geometry("800x600")

# Label

label = tk.Label(root, text="Let the War begin!")
label.pack()

#Text Widget
result_text = tk.Text(root, height=20, width=70, wrap="word")
result_text.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

# Button Click Function
def add_viking():
    viking_name = random.choice(vikingNames) 
    viking = Viking(viking_name, random.randint(1, 100), random.randint(1, 20))
    
    war.addViking(viking)
   
    label.config(text=f"{viking.name} has been added with {viking.health} Health and {viking.strength} Strength")
    result_text.insert(tk.END, f"Viking {viking.name} added with {viking.health} Health and {viking.strength} Strength.\n")

def add_saxon():
    saxon = Saxon(random.randint(1,100),random.randint(1,20))
    war.addSaxon(saxon)
    label.config(text=f"A Saxon has been added to the game wirh {saxon.health} Health and {saxon.strength} Strength")
    result_text.insert(tk.END, f"A Saxon has been added with {saxon.health} Health and {saxon.strength} Strength.\n")
    

def start_game():
    round_of_war = 0
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        war.vikingAttack()
        war.saxonAttack()
        result_text.insert(tk.END, f"Round {round_of_war}: Vikings {len(war.vikingArmy)} vs Saxons {len(war.saxonArmy)}\n")
        war.showStatus()
        round_of_war += 1
    result_text.insert(tk.END, f"Final Status: {war.showStatus()}\n")

# Buttons
viking_button = tk.Button(root, text="Add Viking", command=add_viking)
viking_button.place(relx= 0.5, y=400, anchor = tk.E)

saxon_button = tk.Button(root, text="Add Saxon", command=add_saxon)
saxon_button.place(relx= 0.5, y=400, anchor = tk.W)

war_button = tk.Button(root, text="Let the War begin!", command=start_game)
war_button.place(relx=0.5, y=450, anchor = tk.CENTER)

# Start Tkinter Loop
root.mainloop()
