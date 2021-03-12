def guessing():

# Player 1 picks a number to guess.
    while True:
        try:
            secret = int(input("Player 1, choose a number: "))
            break
        except ValueError:
            print("Must be a whole number.")

# Player 2 guesses a number.        
    while True:
        try:
            guess = int(input("Player 2, guess a number: "))
        except ValueError:
            print("Must be a whole number.")

# The system now checks if the guessed number is correct.
# If not, player 2 is given a hint and guesses again.   
        if guess == secret:
            print("You got it!")
            exit()
        elif guess < secret:
            print("Guess higher!")
        elif guess > secret:
            print("Guess lower!")
        else:
            print("Invalid Option")

# Run the following code only if I run it.
if __name__ == "__main__":
    guessing()