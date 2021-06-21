import math
from davenPort import *
from egz import *
from harbord import *
from egzInf import *

listOfConstants = ["davenPort", "harborth", "egz", "E"]

dicOfConstants = {
    "0": "davenPort",
    "1": "harborth",
    "2": "egz",
    "3": "E"
}


def readRange():
    range = 0
    try:
        while int(range) <= 0:
            range = input('Choose a range (range must be greater then 0): ')
    except ValueError:
        print("Not a number")
    print("Number is :" + str(range))
    return range


def getConstant(constant, listValues, k=0):
    # 0: davenPort
    # 1: harborth
    # 2: egz
    # 3: E
    print(str(constant) + " " + str(listValues) + " " + str(k))
    if int(constant) == 0:
        if len(listValues) == 1:
            return davenPort1(listValues)
        else:
            if checkPrime(listValues):
                return compute_constant(listValues)
            elif len(listValues) == 2:
                return davenPort2(listValues)
            elif len(listValues) == 3:
                return davenPort3(listValues)
            elif len(listValues) == 4:
                return davenPort4(listValues)
            elif len(listValues) == 5:
                return davenPort5(listValues)
            elif len(listValues) == 6:
                return davenPort6(listValues)
            elif len(listValues) == 7:
                return davenPort7(listValues)
            elif len(listValues) == 8:
                return davenPort8(listValues)
            return errorMessage()

    elif int(constant) == 1:
        print("Harbord")

        if len(listValues) == 1:
            return harbord1(listValues)
        elif len(listValues) == 2:
            return harbord2(listValues)
        elif len(listValues) == 3:
            return harbord3(listValues)
        elif len(listValues) == 4:
            return harbord4(listValues)
        return errorMessage()

    elif int(constant) == 2:
        print("EGZ")

        if len(listValues) == 1:
            return egz1(listValues)
        elif checkListEgzMultipowerTwo(listValues):
            return 2 ** len(listValues[1:]) * (int(listValues[0]) + int(listValues[1]) - 2) + 1
        else:

            if len(listValues) == 2:
                return egz2(listValues)
            elif len(listValues) == 3:
                return egz3(listValues)
            elif len(listValues) == 4:
                return egz4(listValues)
            elif len(listValues) == 5:
                return egz5(listValues)
            elif len(listValues) == 6:
                return egz6(listValues)
        return errorMessage()

    elif int(constant) == 3 :
        print("egz <= k(G)")
        if not k:
            return errorMessage("Vous devez saisir une valeur pour k !!")

        return egzInf(listValues, k)

    return errorMessage()


def main():
    CONSTANT = 0  # readConstant()
    RANGE = readRange()


if (__name__ == '__main__'):
    main()
