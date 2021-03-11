def guessing():

# Player 1 picks a number to guess.
    chosen_num = int(input("Player 1, choose a whole number: "))
    secret = chosen_num

    while True:
        guess = int(input("Player 2, guess a whole number: "))
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