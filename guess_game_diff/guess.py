import math

def guessing():

# Player 1 picks a number to guess.
    while True:
        try:
            secret = int(input("Player 1, choose a number between 1 and 100: "))
            break
        except ValueError:
            print("Must be a whole number.")

# Number of tries system shamelessly stolen from Beauseph2187.
# https://github.com/Beauseph2187/
    guessnum = round(math.log(100 - 1 + 1, 2))
    print("\n\tYou have ", guessnum, " chances to guess the number!\n")
    count = 0

# Player 2 guesses a number.        
    while count < guessnum:
        while True:
            if count >= 1:
                print((guessnum - count), "tries remaining.")
            try:
                guess = int(input("Player 2, guess a number: "))
                count += 1
                break
            except ValueError:
                print("Must be a whole number.")

# The system now checks if the guessed number is correct.
# If not, player 2 is given a hint and guesses again.   
        if guess == secret:
            print("\n\tYou Win!\n\nYou got it in ", count, " tries!")
            exit()
        elif guess < secret and count < guessnum:
            print("Guess higher!")
        elif guess > secret and count < guessnum:
            print("Guess lower!")

    if count >= guessnum:
        print("\n\tYou Lost!\n\n0 tries remaining.\nThe number was ", secret, ".")

# Run the following code only if I run it.
if __name__ == "__main__":
    guessing()