# Initialise
file = open("pbook.txt", "w")

pbook_dict = {}

# Add a contact
def addcontact():
    file = open("pbook.txt", "w")
    key = input("Enter contact name :")
    val = input("Enter contact number :")


# Remove a contact
def rmcontact():
    file = open("pbook.txt", "w")
    rm = input("Who would you like to remove? ")
    del pbook_dict[rm]

# Search a contact
def srchcontact(key):
    for index in range (len(pbook_dict)):
        if pbook_dict[index][0] == name :

# Main
def main():
    while True:
        menu = int(input("1. Add a contact\n2. Remove a contact\n3. Search a contact\n4. Exit\n\nEnter your choice: "))
        if menu == 1:
            addcontact()
        elif menu == 2:
            rmcontact()
        elif menu == 3:
            key = input("Search: ")
            srchcontact(key)
        elif menu == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()

for index in range(len(pbook_dict)):
    line = str(pbook_dict[index]) + "\n"
    file.write(line)

file.close()




# Write to file (extra)
