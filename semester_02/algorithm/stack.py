# Made by Chris

#Creating the stack
EMPTYSTRING = ""
NullPointer = -1
MaxStackSize = 8
Stack = ["" for index in range(MaxStackSize - 1)]

#Initialising the stack
BaseOfStackPointer = 0
TopOfStackPointer = NullPointer

#Push an integer into the stack
def Push(NewItem):
    global TopOfStackPointer
    global MaxStackSize
    global menu
    if TopOfStackPointer < MaxStackSize - 1:
        TopOfStackPointer += 1
        Stack[TopOfStackPointer] = NewItem
    menu()
        
#Pop The top most integer of the stack        
def Pop():
    global TopOfStackPointer
    global NullPointer
    global EMPTYSTRING
    global menu
    Item = EMPTYSTRING
    if TopOfStackPointer > NullPointer:
        Item = Stack[TopOfStackPointer]
        TopOfStackPointer = TopOfStackPointer - 1
        menu()
    else:
        print("Unable to pop, since stack has no values")
    menu()

def menu():
    print(Stack)
    option = int(input("Push an item onto the stack [1] or Pop an item off the stack [2]: "))
    if option == 1:
        NewItem = int(input("Input new number: "))
        Push(NewItem)
    elif option == 2:
        Pop()
    else:
        print("Invalid option, please try again")
        menu()

menu()
