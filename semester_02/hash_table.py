# Initialising
CustomerRecord = [[45876, "Chris"], [32390, "Bayu"], [95312, "Ramen"], [64636, "Oreo"], [23467, "Boba"]]
Max = len(CustomerRecord)
HashTable = [0 for i in range(10)]
Record_Loop = 0

def Hash(key):
    Address = key % (10)
    return Address

# Insert a record into a hash table
def Insert(NewRecord):
    global Index
    global CustomerRecord
    global HashTable
    global Record_Loop
    Index = Hash(NewRecord[0])
    while HashTable[Index] != 0:
        Index = Index + 1
        if Index > Max:
            Index = 0
    HashTable[Index] = NewRecord

# Find a record in a hash table
def FindRecord(SearchKey): 
    global Index
    global Max
    global HashTable
    Index = Hash(SearchKey)
    while (HashTable[Index][0] != SearchKey) and HashTable != 0:
        Index += 1
        if Index > Max:
            Index = 0
    if HashTable[Index] != "":
        return HashTable[Index]

def main():
    global Record_Loop
    global HashTable
    global CustomerRecord
    while True:
        print("1. Insert a record into the hash table\n2. Find a record in the hash table\n3. Exit")
        menu = int(input("Enter your choice: "))
        if menu == 1: 
            for i in range(5):
                Insert(CustomerRecord[i])
        elif menu == 2:
            key = int(input("Input key: "))
            FindRecord(key)
        elif menu == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")
        for i in range(len(HashTable)):
            print(i)
main()