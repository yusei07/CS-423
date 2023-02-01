#1 Chris & Bayu ()
NullPointer = -1
Data = ""
List = [["" for col in range(2)]for row in range(7)]

def InitialiseList():
    global StartPointer
    global NullPointer
    global FreeListPtr
    global List
    StartPointer = NullPointer
    FreeListPtr = 0
    for index in range (0, 6):
        List[index][1] = index + 1
    List[6][1] = NullPointer

#2 Filbert (Insert a new node into an ordered linked list)
def InsertNode(NewItem):
    global FreeListPtr
    global NullPointer
    global StartPointer
    global ThisNodePointer
    global PreviousNodePtr
    global NewNodePtr
    global List
    if FreeListPtr != NullPointer:
        NewNodePtr = FreeListPtr
        List[NewNodePtr][0] = NewItem
        FreeListPtr = List[FreeListPtr][1]
        ThisNodePointer = StartPointer
        PreviousNodePtr = NullPointer
        while ThisNodePointer != NullPointer and List[ThisNodePointer][0] < NewItem:
            PreviousNodePtr = ThisNodePointer
            ThisNodePointer = List[ThisNodePointer][1]            
        if PreviousNodePtr == StartPointer:
            List[NewNodePtr][1] = StartPointer       
            StartPointer = NewNodePtr
        else:
            List[NewNodePtr][1] = List[PreviousNodePtr][1]
            List[PreviousNodePtr][1] = NewNodePtr
            
#3 Dylan (Find an element in an ordered linked list)
def FindNode(DataItem):
    global CurrentNodePtr
    global StartPointer
    global NullPointer
    global List
    CurrentNodePtr = StartPointer
    while CurrentNodePtr != NullPointer and List[CurrentNodePtr][0] != DataItem:
        CurrentNodePtr = List[CurrentNodePtr][1]
    return CurrentNodePtr

#4 Marco (Delete a node from an ordered linked list)
def DeleteNode(DataItem):
    global ThisNodePtr
    global StartPointer
    global PreviousNodePtr
    global NullPointer
    global List
    ThisNodePtr = StartPointer
    PreviousNodePtr = None
    while (ThisNodePtr != NullPointer) and (List[ThisNodePtr][0] != DataItem):
        PreviousNodePtr = ThisNodePtr
        ThisNodePtr = List[ThisNodePtr][1]
    if ThisNodePtr != NullPointer:
        if ThisNodePtr == StartPointer:
            StartPointer = List[StartPointer][1]
        else:
            List[PreviousNodePtr][1] = List[ThisNodePtr][1]
        
        List[ThisNodePtr][1] = FreeListPtr
        FreeListPtr = ThisNodePtr


#5 Winc (Access all nodes stored in the linked list)
def OutputAllNodes():
    global CurrentNodePtr
    global StartPointer
    global NullPointer
    global List
    CurrentNodePtr = StartPointer
    while CurrentNodePtr != NullPointer:
        print(List[CurrentNodePtr][0])
        CurrentNodePtr = List[CurrentNodePtr][1]

def main():
    while True:
        InitialiseList()
        what_to_do = int(input("What would you like to do \n 1. Insert A Node: \n 2. Find A Node: \n 3. Delete A Node: \n 4. Output All Nodes: \n"))
        if what_to_do == 1:
            NewItem = str(input("What Node Would You Like To Input: "))
            InsertNode(NewItem)
        elif what_to_do == 2:
            DataItem = str(input("What Node Would You Like To Find? "))
            FindNode(DataItem)
        elif what_to_do == 3:
            DataItem = str(input("What Node Would You Like To Delete: "))
            DeleteNode(DataItem)
        elif what_to_do == 4:
            OutputAllNodes()
        else:
            print("Please input a proper number")

        for i in List:
            print(i)

InitialiseList()
main()