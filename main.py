import random

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
        damage = self.attack - opponent.defense
        if damage < 1:
            damage = 1
        opponent.take_damage(damage)
        print(f"{self.name} attacked {opponent.name} and dealt {damage} damage!")
        if opponent.is_fainted():
            print(f"{opponent.name} fainted!")
    
    def __str__(self):
        return f"{self.name} (lvl {self.level}) with {self.current_hp} / {self.max_hp} HP"

# Define the available Pokemon
pokemons = [
    Pokemon("Bulbasaur", "Grass", 5, 45, 45, 49, 49, 45),
    Pokemon("Charmander", "Fire", 5, 39, 39, 52, 43, 65),
    Pokemon("Squirtle", "Water", 5, 44, 44, 48, 65, 43),
    Pokemon("Pikachu", "Electric", 5, 35, 35, 55, 30, 90)
]

# Choose a random player and opponent Pokemon
player_pokemon = random.choice(pokemons)
opponent_pokemon = random.choice(pokemons)

print("A wild {} appeared!".format(opponent_pokemon.name))
print("I choose you, {}!".format(player_pokemon.name))

# Start the battle
while True:
    # Player's turn
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
    print()
    print(player_pokemon)
    print(opponent_pokemon)
    opponent_pokemon.attack_opponent(player_pokemon)
    if player_pokemon.is_fainted():
        print("You lost the battle!")
        break
