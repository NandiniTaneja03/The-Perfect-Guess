import random

'''
1 for snake
-1 for water 
0 for gun
'''

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

computer = random.choice([-1, 0, 1])  # random computer input
yourstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if yourstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[yourstr]
    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

    if you == computer:
        print("It's a tie")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You Win")
    else:
        print("You Lose")
