import random

computer_rand = random.randint(100, 1000)


for i in range(1,7):
    guessed_number = input("Please enter a three digit guess: ")
    if guessed_number.isdigit() and len(guessed_number) == 3:
        if int(guessed_number) == computer_rand:
            print("congratulation, your guess is right...")
            print(f"number of remained attempt is {6-i}")
            break
        elif int(guessed_number) > computer_rand:
            print("guessed number is bigger than computer number, try again...")
        elif int(guessed_number) < computer_rand:
            print("guessed number is less than computer number, try again...")
    else:
        print("the guess format you entered is not correct, try again...")

    if i==6:
        print(f"Sorry you have used all attempts, The correct number was {computer_rand}")


