# Mini-Project:Guessing Game

import random 

def play_game():
    lucky_number = random.randint(1,50)

    while True:
        user_num=int(input("Guess the lucky_number:"))

        if user_num == lucky_number:
            print("You won.Game Over!!")
        elif user_num < lucky_number:
            print("Too Low")
        else:
            print("Too High")
    print("Thank you for playing.")
play_game()