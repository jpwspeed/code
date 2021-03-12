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
        try:
            guess = int(input("Player 2, guess a number: "))
            count += 1
        except ValueError:
            print("Must be a whole number.")

# The system now checks if the guessed number is correct.
# If not, player 2 is given a hint and guesses again.   
        if guess == secret:
            print("You got it in ", count, " tries!")
            exit()
        elif guess < secret:
            print("Guess higher!")
        elif guess > secret:
            print("Guess lower!")
        else:
            print("Invalid Option")

    if count >= guessnum:
        print("0 tries remaining.\nThe number was ", secret, ".")

# Run the following code only if I run it.
if __name__ == "__main__":
    guessing()