def gcditerative(a,b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcditerative(36, 24))

def gcdrecursive(a, b):
    if b == 0: # base case
        return a
    else:
        return gcdrecursive(b, a % b)
print(gcdrecursive(36, 24))