def guessing():

# Player 1 picks a number to guess. This loops until a
# whole number is entered, where a break moves it along.
    while True:
        try:
            secret = int(input("Player 1, choose a number: "))
            break
        except ValueError:
            print("Must be a whole number.")

# Player 2 guesses a number. This uses a nested while loop.
# The nested loop will loop the guess until a whole
# number is entered. It then continues the original loop,
# allowing player 2 to guess again if they were wrong.       
    while True:
        while True:
            try:
                guess = int(input("Player 2, guess a number: "))
                break
            except ValueError:
                print("Must be a whole number.")  
        if guess == secret:
            print("You got it!")
            exit()
        elif guess < secret:
            print("Guess higher!")
        elif guess > secret:
            print("Guess lower!")
        else:
            print("Invalid Option")

# The else at the end of the loop is used as a catch-all.
# There should be nothing entered that can reach the else.

# Run the following code only if I run it.
if __name__ == "__main__":
    guessing()