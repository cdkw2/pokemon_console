#!/usr/bin/env python
# coding: utf-8

# In[21]:


import random
import os
import time

class Pokemon:
    def __init__(self, name, type, level, max_hp, current_hp, attack, defense, speed):
        self.name = name
        self.type = type
        self.level = level
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_fainted(self):
        return self.current_hp == 0
    
    def attack_opponent(self, opponent):
        is_critical = random.random() < 0.25  # 25% chance of a critical hit, adjust as desired
        damage = self.attack - opponent.defense
        type_chart = {
            "Grass": {"Water": 2.0, "Fire": 0.5, "Electric": 1.0},
            "Water": {"Fire": 2.0, "Grass": 0.5, "Electric": 0.5},
            "Fire": {"Water": 0.5, "Grass": 2.0, "Electric": 1.0},
            "Electric": {"Water": 2.0, "Grass": 1.0, "Fire": 1.0}
        }

        effectiveness = type_chart.get(self.type, {}).get(opponent.type, 1.0)
        damage *= effectiveness

        if is_critical:
            print("Critical Hit!")
            damage *= 2  # Double the damage for a critical hit

        if damage < 1:
            damage = 1

        opponent.take_damage(damage)
        print(f"{self.name} attacked {opponent.name} and dealt {damage} damage!")
        if effectiveness > 1.0:
            print("It's super effective!")
        elif effectiveness < 1.0:
            print("It's not very effective.")
        
        if opponent.is_fainted():
            print(f"{opponent.name} fainted!")
    
    def __str__(self):
        return f"{self.name} (lvl {self.level}) with {self.current_hp} / {self.max_hp} HP"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
# Define the available Pokemon
pokemons = [
    # First Generation
    Pokemon("Bulbasaur", "Grass", 5, 45, 45, 49, 49, 45),
    Pokemon("Charmander", "Fire", 5, 39, 39, 52, 43, 65),
    Pokemon("Squirtle", "Water", 5, 44, 44, 48, 65, 43),
    
    # Second Generation
    Pokemon("Chikorita", "Grass", 5, 45, 45, 49, 65, 45),
    Pokemon("Cyndaquil", "Fire", 5, 39, 39, 52, 43, 65),
    Pokemon("Totodile", "Water", 5, 50, 50, 48, 65, 43),
    
    # Third Generation
    Pokemon("Treecko", "Grass", 5, 40, 40, 45, 35, 70),
    Pokemon("Torchic", "Fire", 5, 45, 45, 60, 40, 45),
    Pokemon("Mudkip", "Water", 5, 50, 50, 70, 50, 40),

    # Fourth Generation
    Pokemon("Turtwig", "Grass", 5, 55, 55, 68, 64, 31),
    Pokemon("Chimchar", "Fire", 5, 44, 44, 58, 44, 61),
    Pokemon("Piplup", "Water", 5, 53, 53, 51, 53, 40),

    # Fifth Generation
    Pokemon("Snivy", "Grass", 5, 45, 45, 45, 55, 63),
    Pokemon("Tepig", "Fire", 5, 65, 65, 63, 45, 45),
    Pokemon("Oshawott", "Water", 5, 55, 55, 55, 45, 45),

    # Sixth Generation
    Pokemon("Chespin", "Grass", 5, 56, 56, 61, 65, 38),
    Pokemon("Fennekin", "Fire", 5, 40, 40, 62, 52, 60),
    Pokemon("Froakie", "Water", 5, 41, 41, 56, 40, 71),

    # Seventh Generation
    Pokemon("Rowlet", "Grass", 5, 68, 68, 55, 50, 42),
    Pokemon("Litten", "Fire", 5, 45, 45, 65, 40, 70),
    Pokemon("Popplio", "Water", 5, 50, 50, 54, 54, 40),

    # Eighth Generation
    Pokemon("Grookey", "Grass", 5, 50, 50, 65, 50, 65),
    Pokemon("Scorbunny", "Fire", 5, 50, 50, 71, 40, 69),
    Pokemon("Sobble", "Water", 5, 50, 50, 40, 40, 70),
]

# Choose a random player and opponent Pokemon
player_pokemon = random.choice(pokemons)
opponent_pokemon = random.choice(pokemons)

print("A wild {} appeared!".format(opponent_pokemon.name))
print("I choose you, {}!".format(player_pokemon.name))

# Start the battle
while True:
    # Player's turn
    cls() # Clear the console
    print()
    print(player_pokemon)
    print(opponent_pokemon)
    print("What will you do?")
    print("1. Attack")
    print("2. Switch")
    choice = input("> ")
    if choice == "1":
        player_pokemon.attack_opponent(opponent_pokemon)
        if opponent_pokemon.is_fainted():
            print("You won the battle!")
            break
    elif choice == "2":
        player_pokemon = random.choice(pokemons)
        print("You switched to {}".format(player_pokemon.name))
    else:
        print("Invalid choice!")
        continue
    
    # Opponent's turn
    cls()  # Clear the console
    print()
    print(player_pokemon)
    print(opponent_pokemon)
    opponent_pokemon.attack_opponent(player_pokemon)
    if player_pokemon.is_fainted():
        print("You lost the battle!")
        break

