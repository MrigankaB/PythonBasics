"""
1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
"""
import random


def play():
    n1 = int(input("Enter you Range, From: "))
    n2 = int(input("                 Till: "))
    num = int(random.randint(n1, n2))
    guess = 1
    ex = 0

    while guess < 6 and ex == 0:
        inp = int(input("Guess the Number: "))
        if inp == num:
            print("Congrats! you guessed the number in ", guess, "chances")
            ex = 1
            again()

        elif inp > num and inp <= n2:
            print("Try Smaller number")
            print("You have ", 5 - guess, "Guesses left!")
        elif inp < num and inp >= n1:
            print("Try Lager number")
            print("You have ", 5 - guess, "Guesses left!")
        else:
            print("Invalid Input!")
            print("You have ", 5 - guess, "Guesses left!")

        guess = guess + 1

    if guess == 6:
        print("Game Over! ")

    #again()


def again():
    play_again = input("Do you want to paly again? Y/N: ")

    if play_again == 'n' or 'N':
        print("Adios!")
    elif play_again == 'y' or 'Y':
        play()
    else:
        print("Give an Input! ")
        again()

play()
#again()

#Error in again() function