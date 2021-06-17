from math import factorial, comb


def multi_coefficient(n: int, lt: list):
    if len(lt) == 0:
        raise Exception("List cannot be empty")
    if len(lt) == 1:
        return comb(n, lt[0])
    return lt
