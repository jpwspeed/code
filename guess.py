def guessing():

# Player 1 picks a number to guess.
    while True:
        num1 = input("Player 1, choose a number: ")
        if num1 == int:
            chosen_num = int(num1)
        else:
            print("Choose a whole number")
            break
    
    while True:
        num2 = input("Player 2, guess a number: ")
        if num2 == int:
            break
        else:
            print("Choose a whole number")
            break
    
    
    secret = chosen_num

    while True:
        guess = int(num2)
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