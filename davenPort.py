from math import gcd as bltin_gcd

def davenPort1(listValues):
    return listValues[0]

def davenPort2(lisValues):
    return compute_constant(lisValues)

def davenPort3(lisValues):
    x = int(lisValues[0])
    y = int(lisValues[1])
    z = int(lisValues[2])
    if x in [2, 3, 4, 6]:
        if int(x) == int(y):
            return compute_constant(lisValues)

        elif ((x == 3) & (x < int(y)) & (y == int(z)) & (bltin_gcd(int(y/3), 6) == 1)):
            return compute_constant(lisValues)
        elif (x * (y**2)-(2*y)-x-2) <= z:
            return compute_constant(lisValues)

        else:
            return "The values does not satisfy the conditions"
    elif (x == y == z):
        list = decompose_number(x)
        if all(val == list[0] for val in list):
            return compute_constant(lisValues)
        #if all(val == list[0] for val in list) & (int(list[0]) == 2) & (len(list)%5 == 0):
        #    return compute_constant(lisValues)

    else:
        return "Other casese are not known"


def compute_constant(lisValues):
    result = 1
    for val in lisValues:
        result += int(val) - 1
    return result

def decompose_number(number=0):
    list = []
    i = 2
    n = number
    while int(n) > 1:
        while n % i == 0:
            n = n / i
            list.append(i)
        i +=1
    return list





