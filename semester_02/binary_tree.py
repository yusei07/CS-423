# Made by Mr. Steven

NullPointer = -1
RootPointer = -1
FreePtr = 0
Tree = [["" for col in range(3)]for row in range(7)]

def InitialiseTree():
    global RootPointer
    RootPointer = NullPointer
    FreePtr = 0
    for Index in range(6):
        Tree[Index][0] = Index + 1
    Tree[6][0] = NullPointer

def InsertNode(NewItem):
    global Tree
    global FreePtr
    global RootPointer
    if FreePtr != NullPointer: #check if there is still space in the array
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr][0]
        Tree[NewNodePtr][1] = NewItem
        print("done")
        Tree[NewNodePtr][0] = NullPointer
        print("done")
        Tree[NewNodePtr][2] = NullPointer
        print("done")
        for cell in Tree:
            print(cell)
        if RootPointer == NullPointer: #check if NewItem is the first(root) of the tree
            RootPointer = NewNodePtr
        else: #if the NewItem is not the root
            ThisNodePtr = RootPointer
            while ThisNodePtr != NullPointer:
                PreviousNodePtr = ThisNodePtr
                if Tree[ThisNodePtr][1] > NewItem:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr][0]
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr][2]

            if TurnedLeft == True:
                Tree[PreviousNodePtr][0] = NewNodePtr
            else:
                Tree[PreviousNodePtr][2] = NewNodePtr
    
InitialiseTree()
for cell in Tree:
    print(cell)

print("===========")
InsertNode("F")
print("FreePtr: ", FreePtr)
print("RootPtr: ", RootPointer)
    
print("===========")
InsertNode("C")
print("FreePtr: ", FreePtr)
print("RootPtr: ", RootPointer)

print("===========")
InsertNode("S")
print("FreePtr: ", FreePtr)
print("RootPtr: ", RootPointer)

print("=====FINAL STATE======")
for cell in Tree:
    print(cell)