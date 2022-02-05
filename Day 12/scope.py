enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside funtion {enemies}")

increase_enemies()
print(f"enemies outside funtion {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

# Global Scope

drink_potion()

player_health = 10
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)
drink_potion()

# There is no Block Scoper

game_lvl = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_lvl < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Modifying global scope(Not Recommended)

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside funtion {enemies}")

increase_enemies()
print(f"enemies outside funtion {enemies}")

# Modifying global scope(Recommended)

enemies = 1

def increase_enemies():
    global enemies
    print(f"enemies inside funtion {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside funtion {enemies}")

# Global Constants

PI = 3.14159
URL = ""
TWITTER_HANDLE = ""


