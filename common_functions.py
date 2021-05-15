def compute_constant(listValues):
    result = 1
    for val in listValues:
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

# Check whether elements in list are divisable by the first element in the list
def checkListIsValid(listValues):
    counter = 1
    for element in listValues:
        if counter >= 1:
            if not isValidElement(int(listValues[counter - 1]), int(listValues[counter])):
                return False
    return True

def checkListEgzMultipowerTwo(listValues):
    x = listValues[0]
    y = listValues[1]

    if isPowerOfTwo(int(x)) and isPowerOfTwo(int(y)) and (int(x) <= int(y)) and checkEquallist(listValues[1:]):
        return True
    return False


def isValidElement(x, y):
    if ((y % x == 0) & (y >= x)):
        print("this is values x y:" + str(x) + ' ' + str(y))
        return True
    else:
        return False


def checkPrime(lst):
    x = 1
    for i in lst:
        x = x * int(i)
    print("the value of x:" + str(x))
    new_lst = pFactors(x)
    print("the value of new_lst:" + str(new_lst))
    if checkEquallist(new_lst):
        return is_prime(int(new_lst[0]))

def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    if n == 1: return [1]
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact

def checkEquallist(lst):
   return lst[1:] == lst[:-1]

def is_prime(a):
    return all(a % i for i in range(2, a))

def isPowerOfTwo(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0