import random 
import os

size = 10
counter = 1

grid = [["."] * size for i in range(size)]

treasure_row = random.randint(0, size - 1)
treasure_col = random.randint(0, size - 1)
print(treasure_row, treasure_col)

print("   ", end="")
for col in range(size):
    print(f"{col:2d}", end="")  
print()
for row in range(size):
    print(f"{row:2d} ", end="") 
    print(" ", end="")  
    for col in range(size):
        print(f"{grid[row][col]} ", end="")  
    print()

for i in range(10):
    print(f"# Attempt {counter}")
    guess_row = int(input("Number of row: "))
    guess_col = int(input("Number of column: "))
    os.system('clear') 
    if guess_row < 0 or guess_row >= size:
        print("Invalid row, try again")
        continue
    if guess_col < 0 or guess_col >= size:
        print("Invalid column, try again")
        continue
    counter += 1

    if guess_row == treasure_row and guess_col == treasure_col:
        grid[guess_row][guess_col] = 'O'
        print("Congratulations, you found the treasure!")
        break
    else:
        grid[guess_row][guess_col] = 'X'
        print("Sorry, that's not the right location. Try again.")

    if counter > 10:
        print("You ran out of guesses tho..\nnt >_<")

    print("   ", end="")
    for col in range(size):
        print(f"{col:2d}", end="") 
    print()
    for row in range(size):
        print(f"{row:2d} ", end="")  
        print(" ", end="")  
        for col in range(size):
            print(f"{grid[row][col]} ", end="")
        print()