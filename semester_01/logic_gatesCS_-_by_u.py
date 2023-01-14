''' 
- user choose the 2 inputs (1/0)
- user choose which gate that is desired for the inputs to be converted into
- the gate produces the output that is based on its characteristics 
'''

import os  

# AND GATE
def AND(input_x, input_y): 
    if(input_y == 1 and input_y == 1):
        print('1')
    else:
        print('0')

# NAND GATE
def NAND(input_x , input_y): 
    if(input_x ==  1 and input_y == 1): 
        print('0') 
    else: 
        print('1')

# OR GATE
def OR(input_x, input_y): 
    if(input_x == 0 and input_y == 0):
        print('0') 
    else:
        print('1') 

# NOR GATE
def NOR(input_x, input_y): 
    if(input_x == 0 and input_y == 0): 
        print('1') 
    else: 
        print('0')

# XOR GATE
def XOR(input_x, input_y): 
    if(input_x != input_y): 
        print('1') 
    else:
        print('0') 

# XNOR GATE
def XNOR(input_x, input_y): 
    if(input_x == input_y): 
        print('1') 
    else: 
        print('0')

# main 
while True: 
    input_x = int(input("Input X: "))
    input_y = int(input("Input Y: "))
    if input_x and input_y != 1 or 0: 
        print("Value error!\nPlease insert only 1/0.\n")
    else: 
        user_input = int(input(
            "Select logic gate: \n\n1.AND\n2.NAND\n3.OR\n4.NOR\n5.XOR\n6.XNOR\n\n0.exit\n\nChoose which number: "))
        os.system('clear') 
        if(user_input == 1):
            print('--------AND GATE-------')
            AND(input_x, input_y)
        elif(user_input == 2):
            print('--------NAND GATE-------')
            NAND(input_x, input_y)
        elif(user_input == 3):
            print('--------OR GATE-------')
            OR(input_x, input_y) 
        elif(user_input == 4):
            print('--------NOR GATE-------')
            NOR(input_x, input_y) 
        elif(user_input == 5):
            print('--------XOR GATE-------')
            XOR(input_x, input_y) 
        elif(user_input == 6):
            print('--------XNOR GATE-------')
            XNOR(input_x, input_y)
        else: 
            break
