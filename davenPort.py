from common_functions import *
from math import gcd as bltin_gcd



def davenPort1(listValues):
    return listValues[0]

def davenPort2(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    if (checkListIsValid(listValues)):
        return compute_constant(listValues)
    elif (bltin_gcd(x,y) == 1):
        return x * y
    else:
        return "Other cases for DavenPort are not known for this range"

def davenPort3(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    if x in [2, 3, 4, 6]:
        if int(x) == int(y):
            return compute_constant(listValues)

        elif ((x == 3) & (x < int(y)) & (y == int(z)) & (bltin_gcd(int(y/3), 6) == 1)):
            return compute_constant(listValues)
        elif (x * (y**2)-(2*y)-x-2) <= z:
            return compute_constant(listValues)
        elif ((bltin_gcd(x, y) == 1) & (bltin_gcd(y, z) == 1)):
            values = []
            prod = x * y * z
            values.append(prod)
            return davenPort1(values)
        else:
            return "The values does not satisfy the conditions"
    elif (x == y == z):
        list = decompose_number(x)
        if all(val == list[0] for val in list):
            return compute_constant(listValues)

        #if all(val == list[0] for val in list) & (int(list[0]) == 2) & (len(list)%5 == 0):
        #    return compute_constant(lisValues)

    else:
        return "Other casese are not known for this range"


def davenPort4(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])

    if (x == y == z == 2) & (r%2 == 0):
        return compute_constant(listValues)
    elif (x == y == z == 3) & (r == 6):
        return compute_constant(listValues) + 1
    else:
        return "Other casese are not known for this range"

def davenPort5(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])
    s = int(listValues[4])

    if (x == y == z == r == 2) & (s % 2 == 0) & ((s/2) % 2 == 0) & ((s/2) < 70):
        return compute_constant(listValues)
    elif (x == y == z == r == 2 ) & (s == 6):
        return compute_constant(listValues) + 1
    elif (x == y == z == r == 2) & (s % 2 == 0) & ((s / 2) >= 70):
        if ((s / 2) % 2 == 0 ):
            return int(2 * (s / 2) + 4)
        else:
            return int(2 * (s / 2) + 5)
    else:
        return "Other casese are not known for this range"


def davenPort6(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])
    s = int(listValues[4])
    t = int(listValues[5])

    if (x == y == z == r == s == 2) & (t == 6):
        return compute_constant(listValues)

def davenPort7(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])
    s = int(listValues[4])
    t = int(listValues[5])
    u = int(listValues[6])

    if (x == y == z == r == s == t == 2) & (u == 6):
        return compute_constant(listValues)

def davenPort8(listValues):
    x = int(listValues[0])
    y = int(listValues[1])
    z = int(listValues[2])
    r = int(listValues[3])
    s = int(listValues[4])
    t = int(listValues[5])
    u = int(listValues[6])
    v = int(listValues[7])

    if (x == y == z == r == s == t == u == 2) & (v == 6):
        return compute_constant(listValues)

# The below functions are used to compute the constant and check wether the
# elements in a list are valid

