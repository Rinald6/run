import time
import random
numbers=[1,2,3,4,5,6]
command=""
while True:
    press=print("The dice is rolling  ")
    print("...")
    time.sleep(1)
    roll_dice=random.choice(numbers)
    print(roll_dice)
    command=input("Type quit to quit the game, else any button to continue:")
    if command=="quit".lower():
        print("The game quit!")
        break