import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Set the number of attempts
attempts = 7

print("Guess the number (between 1 and 100)! You have 7 attempts.")

# Repeat until the user guesses correctly or runs out of attempts
while attempts > 0:
    guess = int(input("Enter your guess: "))   # Take user input

    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break 

    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1  # Reduce the number of attempts

# If attempts are over, reveal the correct number
if attempts == 0:
    print(f"No more attempts left! The correct number was {random_number}.")



