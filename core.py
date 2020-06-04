import math
from davenPort import *
from egz import *

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


def readConstant():
    constant = ""
    try:
        IndexConstant = input('Choose a constant from the list [davenPort:0, harborth:1, egz:2, E:3]: ')
        if IndexConstant <= len(listOfConstants):
            print("The constant is : " + listOfConstants[IndexConstant])
        else:
            print("You must enter a valid value")

    except ValueError:
        print("Not a constant")
    return IndexConstant


# def readValues(var):
#     listValues = []
#     for i in range(0,var):
#         # this check will be applied only when we have 2 or more elements in the list
#         listValues.append(input('Enter value '+ str(i+1) +': '))
#         if (len(listValues) >= 2):
#             if not (isValidElement(listValues[i-1], listValues[i])):
#                 print("Invalid list")
#                 break
#             else:
#                 print("valid element")
#
#     print(listValues)
#     return listValues

def getConstant(constant, rang, listValues):
    # 0: davenPort
    # 1: harborth
    # 2: egz
    # 3: E
    print(str(constant) + " " + str(rang) + " " + str(listValues))
    if int(constant) == 0:

        if int(rang) == 1:
            # listValues.append(input('Enter value : '))
            return davenPort1(listValues)
        else:
            # davenPortValues[str(rang)]['values']

            if checkPrime(listValues):
                print('This is a prime number')
                return compute_constant(listValues)
            elif int(rang) == 2:
                return davenPort2(listValues)
            elif int(rang) == 3:
                return davenPort3(listValues)
            elif int(rang) == 4:
                return davenPort4(listValues)
            elif int(rang) == 5:
                return davenPort5(listValues)
            elif int(rang) == 6:
                return davenPort6(listValues)
            elif int(rang) == 7:
                return davenPort7(listValues)
            elif int(rang) == 8:
                return davenPort8(listValues)
            else:
                return "Not yet implemented"

    elif int(constant) == 2:
        print("EGZ")

        if int(rang) == 1:
            # listValues.append(input('Enter value : '))
            return egz1(listValues)
        else:
            # davenPortValues[str(rang)]['values']

            #if checkPrime(listValues):
            #    print('This is a prime number')
            #    return compute_constant(listValues)
            if int(rang) == 2:
                return egz2(listValues)
            elif int(rang) == 3:
                return egz3(listValues)
            elif int(rang) == 4:
                return egz4(listValues)
            elif int(rang) == 5:
                return egz5(listValues)
            elif int(rang) == 6:
                return egz6(listValues)

            else:
                return "Not yet implemented"
    else:
        return "Not yet implemented"

def main():
    CONSTANT = 0  # readConstant()
    RANGE = readRange()

    # LISTVALUES = readValues(RANGE)
    # checkCase(RANGE, LISTVALUES)
    # getValuesFromDictionnary(CONSTANT, RANGE)


if (__name__ == '__main__'):
    main()
