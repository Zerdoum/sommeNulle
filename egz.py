from common_functions import *
from math import gcd as bltin_gcd



def egz1(listValues):
    x = int(listValues[0])
    return x * 2 - 1

def egz2(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    if (checkListIsValid(listValues)):
        return x * 2 + y * 2 - 3
    else:
        return "Other cases for EGZ are not known for this range"

def egz3(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    decomposer = decompose_number(int(x))

    if ((checkEquallist([x,y])) and (x == 2)):
        if ((z >= 4) and (z%2 == 0)):
            return int(4 * (z / 2) + 3)
    elif (((checkEquallist(listValues)) and (x%2 == 0)) and (x%3 == 0)):
        return int(8 * (x - 1 ) + 1)
    elif ((checkEquallist([x, y, z])) and (x%3 == 0) or (x%5 == 0)):
        return int(9 * (x - 1) + 1)
    else:
        return "Other cases for EGZ are not known for this range"

def egz4(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])
    decomposer = decompose_number(int(x))
    if ((checkEquallist([x,y,z])) and (x == 2)):
        if (r == 4):
            return 13
        if (r == 6):
            return 17
        if ((r >= 72 ) and (r % 2 == 0)):
            return int(4 * (r / 2) + 5)
    elif ((checkEquallist(decomposer)) and ( int(decomposer[0]) == 3) and (checkEquallist(listValues))):
        return 20 * ((3 ** len(decomposer)) - 1 ) + 1
    else:
        return "the condition is not satisfied for this group EGZ"



def egz5(listValues):
    x = int(listValues[0])
    if (checkEquallist(listValues)) & (x == 3):
        return 91
    else:
        return "Other cases for EGZ are not known for this range"

def egz6(listValues):
    x = int(listValues[0])
    if (checkEquallist(listValues)) & (x == 3):
        return 255
    else:
        return "Other cases for EGZ are not known for this range"

def compute_constant(listValues):
    result = 1
    for val in listValues:
        result += int(val) - 1
    return result