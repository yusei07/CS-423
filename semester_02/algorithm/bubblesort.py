ProdNum = [25, 68, 70, 50, 80]

def Bubblesort():
    n = len(ProdNum)
    for i in range(n):
        for j in range(n-1):
            if ProdNum[j] > ProdNum[j+1]:
                ProdNum[j], ProdNum[j+1] = ProdNum[j+1], ProdNum[j]
        n = n -1

Bubblesort()
print(ProdNum)
