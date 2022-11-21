from random import randint

print("CODEBREAKER\nGuess the 4-digit code!\n?-?-?-?")
gen_code = randint(1000, 9999)
print(gen_code) # comment this to play

attempts = 1
while attempts < 13:
    guess = int(input(f"Try #{attempts} - Please enter your guess: "))
    if guess == gen_code:
        print("Yay! You guessed the correct number")
        break
    else:
        gen_code = str(gen_code)
        guess = str(guess)
        correct_digit = 0
        correct_position = 0
        checked_digit = []
        checked_position = []
        for i in range(4):
            if gen_code[i] == guess[i]:
                correct_position += 1
                if guess[i] not in checked_position:
                    checked_position.append(guess[i])
        for i in range(4):
            if guess[i] not in checked_digit:
                for n in range(4):
                    if guess[i] == gen_code[n]:
                        correct_digit += 1
            if guess[i] not in checked_digit:
                checked_digit.append(guess[i])
        print(f"You got {correct_digit} digits correct, and {correct_position} of them are in the right position")
        attempts += 1
else:
    print(f"\nYou ran out of guesses! The correct number is {gen_code}, The game has ended.")
