def power(base, exp):
    if exp == 0:
        result = 1
    else:
        result = base * power(base, exp -1)
    return result
print(power(2, 4))

# iterative ver
# def power(base, exp):
#     result = 1
#     for i in range(exp):
#        result *= base
#     return result
# print(power(2, 4))