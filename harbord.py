from common_functions import *
from math import gcd as bltin_gcd



def harbord1(listValues):
    x = int(listValues[0])
    if (x%2 == 0):
        return x + 1
    return x

def harbord2(listValues):
    x = int(listValues[0])
    y = int(listValues[1])

    if (is_prime(x) and is_prime(y) and checkEquallist(listValues) and ((x >=47) or (x in [3,5,7]))):
        return 2 * x - 1

    elif (checkEquallist(listValues)):
        if (x%2 == 0):
            return 2 * x + 1
        elif (x == 2):
            return 5
        return 2 * x - 1

    elif ((x == 2) and (y%2 == 0)):
        if ((y/2)%2 == 0):
            return y + 2
        return y + 3

    elif ((is_prime(int(y/3))) and (x == 3) and ( y%3 == 0) and ((y/3)!=3)):
        return y + 3

    elif ((x == 3) and (y == 9)):
        return 13

    elif ((x == 3) and (y == 12)):
        return 14

    elif ((x == 6) and (y == 6)):
        return 13

    return errorMessage()

def harbord3(listValues):
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
    elif (x==2,y==z==4):
        return 13
    return errorMessage()


def harbord4(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])

    if (x==y==z==2,r==4):
        return 9
    return errorMessage()
