MyList = [25, 34, 98, 7, 41, 19, 5]
MaxIndex = 7
n = MaxIndex - 1 

for i in range(0, MaxIndex - 1): 
    for j in range(0, n):
        if MyList[j] > MyList[j + 1]:
            Temp = MyList[j]
            MyList[j] = MyList[j + 1]
            MyList[j + 1] = Temp
    n = n - 1 # used to limit the value of j 
print(MyList)