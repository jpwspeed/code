from guess import guessing
from rand import rand_guess

choices = {
    "1": rand_guess,
    "2": guessing
}

while True:
    print("Welcome to the Guessing Game!\n1 for Single Player\n2 for Two Player\nexit to quit")
    option = input("How many players? >")
    if result:= choices.get(option):
        result()
    elif result:= "exit":
        exit()
    else:
        print("Invalid Option")