from common_functions import *
from davenPort import *
from egz import *
from common_functions import *
import math
from math import gcd as bltin_gcd


def egzInf(listValues,k):
    davenport = 0
    k = int(k)
    egzInfList = listValues

    if len(egzInfList) == 1:
        return davenPort1(egzInfList)
    else:
        result = checkEgzInfException(egzInfList,k)
        if result:
            return result
        elif checkPrime(egzInfList):
            print("check prime")
            davenport = compute_constant(egzInfList)
            print(str(davenport))
        elif len(egzInfList) == 2:
            exception = checkEgzInfRangeTwoException(egzInfList,k)
            if exception:
                return exception
            davenport = davenPort2(egzInfList)
        elif len(egzInfList) == 3:
            davenport = davenPort3(egzInfList)
        elif len(egzInfList) == 4:
            davenport = davenPort4(egzInfList)
        elif len(egzInfList) == 5:
            davenport = davenPort5(egzInfList)
        elif len(egzInfList) == 6:
            davenport = davenPort6(egzInfList)
        elif len(egzInfList) == 7:
            davenport = davenPort7(egzInfList)
        elif len(egzInfList) == 8:
            davenport = davenPort8(egzInfList)

    if isinstance(davenport, int):
        if k == int(davenport) - 1:
            return int(davenport) + 1
        elif k >= int(davenport):
            return davenport
    return errorMessage()

def checkEgzInfException(egzInfList,k):
    egzResult = 0
    print("Entered exception for egzInf!!")
    if int(k) == int(egzInfList[-1]):
        if checkListEgzMultipowerTwo(egzInfList):
            egzResult = 2 ** len(egzInfList[1:]) * (int(egzInfList[0]) + int(egzInfList[1]) - 2) + 1
        elif len(egzInfList) == 2:
            egzResult = egz2(egzInfList)
        elif len(egzInfList) == 3:
            egzResult = egz3(egzInfList)
        elif len(egzInfList) == 4:
            egzResult = egz4(egzInfList)
        elif len(egzInfList) == 5:
            egzResult = egz5(egzInfList)
        elif len(egzInfList) == 6:
            egzResult = egz6(egzInfList)

    if int(egzResult):
        return int(egzResult) - int(egzInfList[-1]) + 1

    if (int(egzInfList[0]) == 2) and (checkEquallist(egzInfList)):
        r = len(egzInfList)
        if k in range(math.ceil((2 * r + 2)/3),r + 1):
            return r + 2

    if (int(egzInfList[0]) == 2) and (checkEquallist(egzInfList)) and (k == 3):
        return 2 ** (len(egzInfList)-1) + 1

    if len(egzInfList) == 3:
        if (k == 3):
            if (int(egzInfList[0]) == 3) and (checkEquallist(egzInfList)):
                return 17
        elif (k == 4):
            if (int(egzInfList[0]) == 3) and (checkEquallist(egzInfList)):
                return 10
            elif (int(egzInfList[0]) == 2) and (int(egzInfList[1]) == int(egzInfList[-1]) == 4):
                return 14
            elif (int(egzInfList[0]) == 4) and (checkEquallist(egzInfList)):
                return 22
        elif (k == 5):
            if (int(egzInfList[0]) == 3) and (checkEquallist(egzInfList)):
                return 9
            elif (int(egzInfList[0]) == 2) and (int(egzInfList[1]) == int(egzInfList[-1]) == 4):
                return 11
            elif (int(egzInfList[0]) == int(egzInfList[1]) == int(egzInfList[2]) == 2) and (int(egzInfList[-1]) == 4):
                return 9
        elif (k == 6):
            if (int(egzInfList[0]) == 3) and (checkEquallist(egzInfList)):
                return 8
            elif (int(egzInfList[0]) == 2) and (int(egzInfList[1]) == int(egzInfList[-1]) == 4):
                return 10
            elif (int(egzInfList[0]) == 3) and checkEquallist(egzInfList[:-1]) and ( int(egzInfList[-1]) == 6):
                return 14
        elif (k == 7):
            if (int(egzInfList[0]) == 3) and checkEquallist(egzInfList[:-1]) and ( int(egzInfList[-1]) == 6):
                return 13
        elif (k == 8):
            if (int(egzInfList[0]) == 3) and checkEquallist(egzInfList[:-1]) and ( int(egzInfList[2]) == 6):
                return 12
    elif len(egzInfList) == 4:
        if (k == 4):
            if (int(egzInfList[0]) == 2) and checkEquallist(egzInfList[:-1]) and (int(egzInfList[-1]) == 4):
                return 10
        if (k == 5):
            if (int(egzInfList[0]) == 2) and checkEquallist(egzInfList[:-1]) and (int(egzInfList[-1]) == 4):
                return 9
        if (k == 6):
            if (int(egzInfList[0]) == 2) and checkEquallist(egzInfList[:-1]) and (int(egzInfList[-1]) == 6):
                return 12
        if (k == 7):
            if (int(egzInfList[0]) == 2) and checkEquallist(egzInfList[:-1]) and (int(egzInfList[-1]) == 6):
                return 11

    return False


def checkEgzInfRangeTwoException(egzInfList,k):
    davenport = davenPort2(egzInfList)
    diff = davenport - k
    if diff in range(int(egzInfList[0])):
        return davenport + diff
    return False