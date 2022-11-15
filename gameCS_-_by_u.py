'''
- computer generates a number between 15 - 25
- user enters a number from 1 - 3 for the number that is generated to be subtracted as
- computer then choose its own number from 1 - 3 (randomly) for the number to be subtracted as
- loop until the number is below 0, and the last person that subtracted the number lose
'''

import random
import os

generated_num = random.randint(15, 25) 
print("Generated number -->", generated_num)

def dictionary_opt():
    my_dictionary = {'y':'You entered yes!', 'n': 'Welp, have a good one!'}

    while True:
      val = input("Do you wanna play again?\n\n(y) Yes (n) No\n")
      if(val.lower() in ['y', 'n']):
              print(my_dictionary[val])
      else:
          if(not val.lower() == 'y'):
            break
            

def main():
    while True:
      user_num = int(input("Enter a number between 1 - 3: ")) 
      if(user_num == 1 or 2 or 3):
          global generated_num 
          generated_num = generated_num - user_num
          print("Current number:", generated_num)
          if(generated_num < 1):
              os.system('clear')
              print("You Lose!")
              dictionary_opt()
          else:
              computer_num = random.randint(1, 3)
              print("Computer chose", computer_num)
              print("Current number:", generated_num - computer_num)
              if(generated_num < 1):
                  os.system('clear')
                  print("You Win!")
                  dictionary_opt()
      else:
          if(user_num < 1 or user_num > 3):
              print("Number isn't in range. Please try again.")
              break
main()