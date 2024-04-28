# IMPORTS
import sys
import time
import random

# COSMETIC CODE

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def load_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.50)
    print()

# Variables, Classes, Objects

class player_model:
    def __init__(self, inputStrength, inputFortitude, inputAgility, inputWillpower, inputCharisma, inputIntelligence):
        self.str = int(inputStrength)
        self.ftd = int(inputFortitude)
        self.agl = int(inputAgility)
        self.wlp = int(inputWillpower)
        self.cha = int(inputCharisma)
        self.int = int(inputIntelligence)

    def SayWound(self):
        Wound_Phrase = ["Argh!", "Ugh!", "Oof!", "Agh!"]
        print(random.choice(Wound_Phrase))

class factionless_reg_hum_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["No Wait!", "Please!", "Dont!", "Dont please!", "wait! Wait! Wait!"]
        print(random.choice(Beg_Life))

class theheinrich_reg_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "Bitte, töte mich nicht.. [I don't wanna die..]", "Please.. No..", "I can't die now..", "... Avenge Us.. König Heinrich."]
        print(random.choice(Beg_Life))

class theheinrich_loyal_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "Für den König! [For The King!]", "You will not win...", "Heinrich will make you pay..", "Go to hell.."]
        print(random.choice(Beg_Life))

class theheinrich_hr_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "Die Ritter werden dich mitnehmen. [The Knights Will Take You.]", "You will not win...", "Heinrich will make you pay..", "Go to hell.."]
        print(random.choice(Beg_Life))

class abyssaloutcast_reg_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "No.. Dont!", "Have mercy!", "*The Body Was Consumed The Abyss below before they could say a word*"]
        print(random.choice(Beg_Life))

class abyssaloutcast_loyal_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "The Abyss shall return to you.", "*The Sudden Dread of The Abyss Dawns On You", "You will regret this.", "Go to hell.."]
        print(random.choice(Beg_Life))

class abyssaloutcast_hr_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["...", "*The Body Explodes Into Pieces Upon Death*", "*The Sudden Dread of The Abyss Dawns On You"]
        print(random.choice(Beg_Life))

class trialsofone_weakenedmonster_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["*Upon The Death of The Creature You Recieve Blessings of EXP*"]
        print(random.choice(Beg_Life))

class monster_low_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["*The Creature Howls in Pain Seemingly Not Wanting To Die*"]
        print(random.choice(Beg_Life))

class monster_medium_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["*The Creature Stares At You With A Sharp Gaze*"]
        print(random.choice(Beg_Life))

class monster_high_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

    def SayBeg(self):
        Beg_Life = ["*The Creature Mumbles Somehing, as if it learned how to speak.*", "C-cu@*! yo30. *The Creature tried to speak*"]
        print(random.choice(Beg_Life))

class boss_enemy_model:
    def __init__(self, inputDamage, inputHealth, inputPhase):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)
        self.phase = inputPhase
                # Phase 2? [TRUE/FALSE]
            # POSSIBLE QUOTES:
            # - GREAT ENEMY FELLED

# TEMP_Variables

player = player_model(1, 1, 1, 1, 1, 1)

# Definitions

def freigbenpowersfight():
    if freigeben == "A - The Almighty":
        s1 = 20 + player.int * (( 20 / 100 )* 10)
        s2 = 60 + player.str * (( 60 / 100) * 10 )
        s3 = 10 + player.int * (( 10 / 100) * 10 )

# SKILL DPS SCALING FORMULA:  base dmg + attribute points * ( ( base dmg / 1000 ) * 4 )


# Class Path {ORIGIN}

print("You find yourself floating in the abyss, waiting for your soul to awaken.")
print()
print("Create your name:")
username = input("> ")

print("Your Conciousness is adrift... choose the path you shall take.")
print("<1> Heinrich Kingdom [THE KNIGHTS]")
print("<2> The Abyssal Outcasts [THE MERCENARIES]")

player_origin = input("> ") 

if player_origin == "1":
    print("You are born into the Heinrich Kingdom, a valiant knight.")
    print("Your Objective Is To Protect The Kingdom of Heinrich and wipe out ALL threats.")
    print("The path of mercy is not an option, the King's blood flows through all of you, giving you your power.")
    delay_print("The 'Freigeben'")

    freigbenpowers = ["A - The Antithesis", "F - The Fear", "P - The Power"]
    freigeben = random.choice(freigbenpowers)

    delay_print("You have a power within you.")
    delay_print(freigeben)

    if freigeben == "A - The Antithesis":
        delay_print("The Ability To Reverse All Events Towards Your Enemy and The Most Powerful Ability.")
        player = player_model(20, 30, 40, 50, 25, 40)
    
    if freigeben == "F - The Fear":
        delay_print("The Ability To Instill Fear Into Those Who See You.")
        player = player_model(30, 15, 20, 60, 10, 45)
    if freigeben == "P - The Power":
        delay_print("The Ability To Overpower and Kill Those Who Defy You.")
        player = player_model(60, 60, 60, 30, 10, 25)