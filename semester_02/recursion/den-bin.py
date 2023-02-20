def x(n):
    if n == 0 or n == 1: # base case
        print(n)
    else:
        x(n // 2)
        print(n % 2)
x(19)
