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

def egz4(listValues):
    x = int(listValues[0])
    decomposer = decompose_number(int(x))
    if ((checkEquallist(decomposer)) and ( int(decomposer[0]) == 3) and (checkEquallist(listValues))):
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