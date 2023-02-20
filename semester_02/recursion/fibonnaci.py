def fibonacci(num):
    if num <= 1: # base case
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

user_input = int(input("Enter the nth number: "))
for i in range(user_input):
    print(fibonacci(i), end = " ")
