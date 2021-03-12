import random
import math
from difficulty import *

# random module imported
# for random number generation
# math module imported for number of
# tries system

choices = {
    "easy": dif_e_gn,
    "medium": dif_m_gn,
    "hard": dif_h_gn,
    "lucky": dif_lucky_gn,
    "custom": dif_c_gn
}

while True:
    print("\n\tSelect a difficulty level\neasy\nmedium\nhard\nlucky for I'm Feeling Luck (1 guess)\ncustom to set your own difficulty")
    option = input("Enter a difficulty: ")
    if result:= choices.get(option):
        result()
    elif result:= "exit":
        exit()
    else:
        print("Invalid Option")

def rand_guess():
# random number generated to guess
# the random number is generated on each run
    secret = random.randrange(1,100)

# Number of tries system shamelessly stolen from Beauseph2187.
# https://github.com/Beauseph2187/
    guessnum = round(math.log(100 - 1 + 1, 2))
    print("\n\tYou have", guessnum, "chances to guess the number!\n")
    count = 0

    while count < guessnum:
        while True:
            if count >= 1:
                print((guessnum - count), "tries remining.")
            try:
                guess = int(input("Guess a number: "))
                count += 1
                break
            except ValueError:
                print("Must be a whole number.")
        if guess == secret:
            print("\n\tYou Win!\n\nYou got it in", count, "tries!")
            exit()
        elif guess < secret and count < guessnum:
            print("Guess higher!")
        elif guess > secret and count < guessnum:
            print("Guess lower!")

    if count >= guessnum:
        print("\n\tYou Lost!\n\n0 tries remaining.\nThe number was ", secret, ".")

# Run the following code only if I run it.
if __name__ == "__main__":
    rand_guess()