import sys
import random
from enum import Enum

class ENG(Enum):
    ROCK = 1
    PAPER = 2
    CSISSORS = 3

# print("")
# print(ENG(2))
# print(ENG.ROCK)
# print(ENG['ROCK'])
# print(ENG.ROCK.value)
# sys.exit()

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     CSISSORS = 3

# print("")
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print("")
playerchoice = input("Enter ... \n1 for Rock, \n2 for paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.") 

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")
 
# if player == 1:
#     print("you win!")
# else:
#     print("Python wins!")

if player == 1 and computer == 3:
    print("🏆 You win!")
elif player == 2 and computer == 1:
    print("🏆 You win!")
elif player == 3 and computer == 2:
    print("🏆 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 python wins!")
print("")
