import random

target_number = random.randint(1, 9)

print("Guess the number between 1 and 9!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print("That's right!!!")
            break
    except ValueError:
        print("Invalid input :(")
