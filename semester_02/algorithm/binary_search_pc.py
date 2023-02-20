# first = lower bound 
# last = upper bound
# to find the middle

List = [7, 12, 19, 23, 27, 33, 37, 41, 45, 56, 59, 60, 62, 71, 75, 80, 84, 88, 92, 99]
MaxItems = 20
Found  = False
SearchFailed = False
First = 0
Last = MaxItems - 1 
SearchItem = int(input("Search item: "))
Counter = 0

while Found == False and SearchFailed == False:
    Counter += 1
    print(Counter)
    Middle = (First + Last) // 2
    if List[Middle] == SearchItem:
        Found = True
    else:
        if First > Last:
            SearchFailed = True
        else:
            if List[Middle] > SearchItem:
                Last = Middle - 1
            else:
                First = Middle + 1              
if Found == True:
    print(f"Item position: {Middle}")
else:
    print("Item not present in array")