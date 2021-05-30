from common_functions import *
from davenPort import *
from math import gcd as bltin_gcd

egzInfExceptions = [[3,3,3]]


def egzInf(listValues):
    davenport = 0
    k = int(listValues[0])
    egzInfList = listValues[1:]

    if len(egzInfList) == 1:
        return davenPort1(egzInfList)
    else:
        result = checkEgzInfException(k,egzInfList)
        if result:
            return result
#        elif checkPrime(egzInfList):
#            print("check prime")
#            davenport = compute_constant(egzInfList)
#            print(str(davenport))
        elif len(egzInfList) == 2:
            print("Entred case two")
            exception = checkEgzInfRangeTwoException(k, egzInfList)
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
        else:
            return "This case is unknown !!!"

    if k == int(davenport - 1):
        return davenport + 1
    elif k >= int(davenport):
        return davenport

def checkEgzInfException(k,egzInfList):
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


def checkEgzInfRangeTwoException(k, egzInfList):
    davenport = davenPort2(egzInfList)
    diff = davenport - k
    if diff in range(int(egzInfList[0])):
        return davenport + diff
