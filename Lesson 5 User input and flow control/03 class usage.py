import sys
import random
from enum import Enum

class ENG(Enum):
    ROCK = 1
    PAPER = 2
    CSISSORS = 3

print("")
print(ENG(2))
print(ENG.ROCK)
print(ENG['ROCK'])
print(ENG.ROCK.value)
# sys.exit()

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    CSISSORS = 3

print("")
print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
sys.exit()
