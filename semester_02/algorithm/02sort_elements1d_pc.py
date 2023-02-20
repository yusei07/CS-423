MyList = [5, 34, 98, 7, 41, 19, 25]
MaxIndex = len(MyList)

n = MaxIndex - 1
NoMoreSwaps = False

while NoMoreSwaps == False:
    print(MyList)
    NoMoreSwaps = True
    for j in range(n):
        if MyList[j] > MyList[j + 1]:
            MyList[j], MyList[j + 1] = MyList[j + 1], MyList[j] # swapping 
            NoMoreSwaps = False
        print("     ", MyList)
    n = n - 1 # used to limit the value of j 
print(MyList)
