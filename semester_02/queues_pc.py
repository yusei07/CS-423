EMPTYSTRING = ""
NullPointer = -1
MaxQueueSize = 8 
FrontOfQueuePointer = 0 # Points to the front of the queue
EndOfQueuePointer = 0 # Points to the end of the queue
NumberInQueue = 0 # Stores number of items in the queue
# counter var (?)

Queue = [" " for i in range(MaxQueueSize - 1)]

def InitialiseQueue():
    global FrontOfQueuePointer
    global EndOfQueuePointer
    FrontOfQueuePointer = 0
    EndOfQueuePointer = NullPointer 
    NumberInQueue = 0 

# Add item to queue
# adds an item to the end of the queue if there is space in the queue.

def AddToQueue(NewItem):
    global NumberInQueue
    global EndOfQueuePointer
    if NumberInQueue < MaxQueueSize: # Checks if there is space in queue
        EndOfQueuePointer = EndOfQueuePointer + 1 # It increments EndOfQueuePointer by 1
        if EndOfQueuePointer > MaxQueueSize - 1: # If EndOfQueuePointer is greater than 7 it sets it back to 0.
            EndOfQueuePointer = 0
        Queue[EndOfQueuePointer] = NewItem # Adds NewItem to Queue at position EndOfQueuePointer 
        NumberInQueue = NumberInQueue + 1 # Increments NumberInQueue by 1

# Remove item from the queue
# removes an item from the front of the queue if there are items in the queue.

def RemoveFromQueue():
    global NumberInQueue
    global FrontOfQueuePointer
    Item = EMPTYSTRING
    if NumberInQueue > 0: # Checks if queue is empty or not 
        Item = Queue[FrontOfQueuePointer]
        #Queue[FrontOfQueuePointer] = " "
        NumberInQueue = NumberInQueue - 1
        if NumberInQueue == 0:
            InitialiseQueue()
        else:
            FrontOfQueuePointer = FrontOfQueuePointer + 1
            if FrontOfQueuePointer > MaxQueueSize - 1:
                FrontOfQueuePointer = 0
    return Item

def Menu():
    while True:
        print("1. Add item to queue\n2. Remove item from queue\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item to be added: ")
            AddToQueue(item)
            print("Queue:", Queue)
            print("============================================")
        elif choice == 2:
            item = RemoveFromQueue()
            if item == EMPTYSTRING:
                print("Queue is empty")
            else:
                print("Item removed: ", item)
                #print("Queue: ", Queue) 
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

InitialiseQueue()
Menu()