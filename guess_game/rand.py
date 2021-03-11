import random  
# random module imported
# for random number generation

def rand_guess():
# random number generated to guess
# the random number is generated on each run
    randomNum = random.randrange(1,100)
    secret = randomNum

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
    rand_guess()