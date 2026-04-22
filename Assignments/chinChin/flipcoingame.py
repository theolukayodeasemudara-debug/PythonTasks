import random

player_num = int(input("Pick a number between 0 and 1 to play this game of flipping a coin: "))

# Generating a number between 0 and 1
random_num = random.randint(0, 1)

# coin sides
up = "Head"
down = "Tail"

# checking player input
if random_num == 1:
    print(f"No chosen = {player_num} : Comp chose = {random_num}: {up} \n\n You Won!!!")
elif random_num == 0:
    print(f"No chosen = {player_num} : Comp chose = {random_num}: {down} \n\n You lost!!!")
