import random
'''
1 for snake
-1 for water 
0 for gun'''

computer = random.choice([-1,0,1]) #random cupter input 
yourstr = input("Enter your choice") #my input
youDict = {"s":1, "w": -1, "g": 0} #my input dictionary
reverseDict = {1:"snake", -1:"water", 0:"gun"} #computer input dictionary

you = youDict[yourstr] #my input in number form
print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")
if you == computer:
    print("It's a tie")
else:
    if(computer  == -1 and you == 1): 
        print("You Win")
    elif(computer == -1 and you == 0): 
        print("You Lose")
    elif(computer == 0 and you == 1):
        print("You Lose")
    elif(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 1 and you == 0):
        print("You Win")    
    elif(computer == 1 and you == -1): 
        print("You Lose")
    else:
        print("Invalid Input")


