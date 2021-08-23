from math import factorial, comb


def multi_coefficient(n: int, lt: list):
    if len(lt) == 0:
        raise Exception("List cannot be empty")
    if len(lt) == 1:
        return comb(n, lt[0])
    total = 1
    for item in lt:
        total = total*factorial(item)
    return int(factorial(n) / total)

def factorize(num):
    return [n for n in range(1, num + 1) if num % n == 0]