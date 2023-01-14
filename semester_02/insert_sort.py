List = [53, 21, 60, 18, 42, 19]
NumberOfItems = len(List)

for Pointer in range(1, NumberOfItems):
    ItemToBeInserted = List[Pointer]
    CurrentItem = Pointer - 1
    while (List[CurrentItem] > ItemToBeInserted) and (CurrentItem > -1):
        List[CurrentItem + 1] = List[CurrentItem]
        CurrentItem = CurrentItem - 1
    List[CurrentItem + 1] = ItemToBeInserted
print(List)