import random

player_num = int(input("Pick a number between 0 and 3 to play 'Rock--1' 'Paper--2' 'Scissors--3': "))

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
random_num = random.randint(1, 3)

print(f"Comp: {choices[random_num]} ({random_num}),  player: {choices.get(player_num, 'Invalid')} ({player_num})")

if player_num == random_num:
    print("It's a tie")
elif (player_num == 1 and random_num == 3) or (player_num == 2 and random_num == 1) or (player_num == 3 and random_num == 2):
    print("You win!")
elif player_num in [1, 2, 3]:
    print("You lose!")
else:
    print("Invalid input. Pick 1, 2, or 3")
