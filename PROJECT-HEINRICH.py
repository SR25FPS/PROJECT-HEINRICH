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
        self.health = 100

    def SayWound(self):
        Wound_Phrase = ["Argh!", "Ugh!", "Oof!", "Agh!"]
        print(random.choice(Wound_Phrase))

    def fight(self, enemy_var_name):
        while self.health > 0 and globals()[enemy_var_name].hp > 0:
            damage = self.str * 5
            globals()[enemy_var_name].hp -= damage
            print(f"Player deals {damage} damage to {enemy_var_name}")
            if globals()[enemy_var_name].hp <= 0:
                print(f"{enemy_var_name} has been defeated!")
                break
            damage = globals()[enemy_var_name].dmg
            self.health -= damage
            print(f"{enemy_var_name} deals {damage} damage to Player")
            if self.health <= 0:
                print("Player has been defeated!")
                sys.exit()

class factionless_reg_hum_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class theheinrich_reg_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class abyssaloutcast_reg_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class trialsofone_weakenedmonster_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class monster_low_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class monster_medium_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

class monster_high_enemy_model:
    def __init__(self, inputDamage, inputHealth):
        self.dmg = int(inputDamage)
        self.hp = int(inputHealth)

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
Trialsofone = trialsofone_weakenedmonster_enemy_model(5, 25)
Bandit = factionless_reg_hum_enemy_model(10, 30)
Heinrich = theheinrich_reg_enemy_model(15, 70)
HighMonster = monster_high_enemy_model(20, 85)
Abyssaloutcast = abyssaloutcast_reg_enemy_model(25, 100)

# Fighting the monsters

player.fight("Trialsofone")
player.fight("Bandit")
player.fight("Heinrich")
player.fight("HighMonster")
player.fight("Abyssaloutcast")

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
