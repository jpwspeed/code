def guessing():

# Number to guess.
    secret = 42

    while True:
        guess = int(input("Guess a number: "))
        if guess == secret:
            print("You got it!")
            exit()
        elif guess < secret:
            print("Guess higher!")
        else:
            print("Guess lower!")

# Run the following code only if I run it.
if __name__ == "__main__":
    guessing()