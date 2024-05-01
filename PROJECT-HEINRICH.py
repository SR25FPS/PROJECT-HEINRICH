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

hollowfication = 0

staminanone = ["You got too tired and your body missed it's hit."]

class player_model:
    def __init__(self, str, dex, sta, wis, cha, health):
        self.str = str
        self.dex = dex
        self.sta = sta
        self.wis = wis
        self.cha = cha
        self.health = 10000


    def SayWound(self):
        Wound_Phrase = ["Argh!", "Ugh!", "Oof!", "Agh!"]
        print(random.choice(Wound_Phrase))
    
    
    def fight(self, enemy_var_name):
        Stamina = self.sta * 30
        enemy = globals()[enemy_var_name]
        print(f"{enemy_var_name} has come to challenge you")
        print("Will you fight or will you try to run?")
        choice = input("[F/R]")
        if choice == "F":
            fr = input(f"Are you sure you want to challenge {enemy_var_name} [F/R]")
            exit = 0
            while self.health > 0 and enemy.hp > 0 and exit == 0:
                # Turn Based Code
                Dexterity = self.dex
                Wisdom = self.wis
                Option = input("A: Fight \n"
                               "B: Dodge \n"
                               "C: Run")
                # Enemy
                damagemin = self.str * 3
                damagemax = self.str * 5
                if Option == "A" and Stamina > 0:
                    damage = random.randint(damagemin, damagemax)
                    enemy.hp -= damage
                    if stamina < 0:
                        print("Not Enough Stamina For That!, you dealt no damage!")
                    if stamina > 0:
                        if damage == damagemax:
                            print(f"Critical hit! Player dealt {damage} damage to {enemy_var_name}")
                        else:
                            print(f"Player deals {damage} damage to {enemy_var_name}")
                    damage = enemy.dmg
                    self.health-= damage
                    Stamina -= 7
                # Player
                damage = enemy.dmg
                if Option == "B":
                    if Dexterity <= 1:
                        DodgeChance = random.randint(1, 5)
                        if DodgeChance == 3:
                            damage = 0
                            print("You succesfully dodged the enemies attack")
                            Stamina -= 5
                        else:
                            self.health -= damage
                            Stamina -= 10
                    if Dexterity >= 2 and Dexterity <= 5:
                        DodgeChance = random.randint(1, 2)
                        if DodgeChance == 2:
                            damage = 0
                            print("You succesfully dodged the enemies attack")
                            Stamina -= 5
                        else:
                            self.health -= damage
                            Stamina -= 10
                if not Stamina == 0:
                    print(f"{enemy_var_name} dealt {damage} damage to Player")
                    print(f"Player has {self.health} HP left")
                    print("Player has", Stamina, "stamina left")
                    if enemy.hp <= 0:
                        enemy.hp = 0
                    print(f"{enemy_var_name} hp is {enemy.hp}, The gods are cheering you on")
                    if enemy.hp <= 0:
                        print(f"{enemy_var_name} has been defeated!")
                        break
                    if self.health <= 0:
                        print("Player has been defeated!")
                        sys.exit()
                else:
                    print("You have been defeated")
        else:
            print("You successfully ran away but you feel something disappointed within you.")
            global hollowfication
            hollowfication += 1  # increment hollowfication by 1

            if hollowfication == 1:
                delay_print("You feel a sharp pain in your chest, warning you to stop running.")

            if hollowfication == 2:
                delay_print("You feel a heavy pain in your heart making your conciousness hazy.")

            if hollowfication == 3:
                delay_print("???: Stop Running Coward. I did not posses and give you power for you to run away from a fight.")
                delay_print("???: You WILL fight.")

            if hollowfication > 3:
                delay_print("You feel a heavy pain in your chest, your body slowly losing it's power.")
                delay_print("You walk closer to death as you get on your knees taking your final breath.")
                delay_print("???: I warned you.")
                delay_print("Your Chest produces a hollow hole of emptiness, your body lies there nothing more than a mere corpse in the world of bloodshed.")
                print()
                print("ENDING: UNWORTHY, Rejected by One's Own Blood. (1/4)")
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
# player.fight("Abyssaloutcast")


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

print("Your Conciousness is adrift...")

delay_print("You are born into the Heinrich Kingdom, a valiant knight.")
print("Your Objective Is To Protect The Kingdom of Heinrich and wipe out ALL threats.")
delay_print("The path of mercy is not an option, the King's blood flows through all of you, giving you your power.")
delay_print("The 'Freigeben'")

freigbenpowers = ["A - The Antithesis", "F - The Fear", "P - The Power",]
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

delay_print("You awake, in a place where all warriors are trained.")
print("- The Trials of One -")
delay_print("A place where warriors are made.")
print()
print()
delay_print("The Voice of Heinrich: Ah.. a fresh soul, what's keeping you from within?")
delay_print("Strip away your belongings and we shall begin.")
print("Skip Tutorial? [Y/N]")

while True:

    skip_tut = input("> ")
    if skip_tut == "Y":
        delay_print("The Voice of Solitude: Let us begin.")
        delay_print("You feel a slight spiritual pressure, a tingle in your body.")
        delay_print("You see the one generating such pressure.. A Beast of Great Size, A Shark-Like Being with massive claws standing on two legs with corals growing from it's back.")
        player.fight("Trialsofone")

    if skip_tut == "N":
        break

    else:
        delay_print("The Voice of Solitude: What was that? Repeat. [Y/N]")
        print()

