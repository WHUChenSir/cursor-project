import random

print("Welcome to Guess the Number!")
print("I picked a number between 1 and 20.")

target = random.randint(1, 20)
attempts = 0

while True:
    guess_text = input("Your guess: ")

    if not guess_text.isdigit():
        print("Please enter a whole number.")
        continue

    guess = int(guess_text)
    attempts += 1

    if guess < target:
        print("Too low, try again.")
    elif guess > target:
        print("Too high, try again.")
    else:
        print(f"You got it in {attempts} tries. Nice!")
        break