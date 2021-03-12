import math
from guess import guessing
from rand import rand_guess

def custom_dif():
    while True:
        try:
            upper = int(input("Enter the highest number possible: "))
            break
        except ValueError:
            print("Must be a whole number.")
    while True:
        try:
            lower = int(input("Enter the lowest number possible: "))
            break
        except ValueError:
            print("Must be a whole number.")
    round(math.log(upper - lower +1, 2))
    return int

dif_c_gn = custom_dif()

dif_e_gn = 7,
dif_m_gn = 5,
dif_h_gn = 3,
dif_lucky_gn = 1,
    