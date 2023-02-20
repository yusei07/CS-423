my_list = [4, 6, 13, 5, 8, 3]

max_index = 6
search_value = int(input("Enter the value: "))

found = False 
index -= 1

while (found == False) and (index  < max_index):
    if my_list[index] == search_value:
        found = True
    else:
        index += 1

if found = True:
    print(f"Value found at location: {index}")
else: 
    print("Value not found")


    
    index += 1
    if my_list[index] == search_value:
        found = True


    print(f"Value found at location: {index}")

    else:
        print("Value not found")
