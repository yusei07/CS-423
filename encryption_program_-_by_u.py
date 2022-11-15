from random import randint
import os

cipher = [
"A", "1", "B", "2", "C", "3", "D", "4", "E", "5", 
"F", "6", "G", "7", "H", "8", "I", "9", "J", "0", 
"K", "a", "L", "b", "M", "c", "N", "d", "O", "e", 
"P", "f", "Q", "g", "R", "h", "S", "i", "T", "j", 
"U", "k", "V", "l", "W", "m", "X", "n", "Y", "o", 
"Z", "p", "q", "!", "r", ".", "s", "," , "t", "<", 
"u", ">", "v", "/", "w", "-", "x", "[", "y", "_", 
"z", "+", "=", "(", ")", "]", ":", ";", "*", "&", 
"^", "%", "$", "#", "@", "'", "?", "{", "}"
] 

def encrypt():
    f_key = randint(10, 21)
    s_key = f_key-7
    plain_text = input("Input text: ")
    var_a = "" 
    for i in range(len(plain_text)):
        temp_b = cipher.index(plain_text[i])-f_key
        var_a = var_a + cipher[temp_b%88]
    print("cipher text: ", var_a) 
    print("Encryption key is: ", s_key)

def decrypt():
    key_f = int(input("Encryption key: "))
    key_s = key_f+7
    cipher_text =(input("Input text: "))
    var_b = ""
    for i in range(len(cipher_text)):
        temp_b = cipher.index(cipher_text[i])+key_s
        var_b = var_b + cipher[temp_b%88]
    print("Plaintext: " + var_b )

def main():
    while True: 
        menu = input("\n Do you want to encrypt or decrypt?\n 1. Encrypt\n 2. Decrypt\n\n 0. Exit program.\n")
        os.system('clear')
        if menu == '1':
            encrypt()
        elif menu == '2':
            decrypt()
        else:
            break

main()

# sankyuu chris!