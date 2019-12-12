import random

secretNumber = random.randint(1, 20)
print("I have a number between 1 and 20")

# Give the player 7 guesses
for guessesRemaining in range(7, -1, -1):
    guess = int(input("Take a guess: "))

    if guess > secretNumber:
        print("Your guess was too high")
    elif guess < secretNumber:
        print("Your guess was too low")
    # Must have guessed correctly
    else:
        break

    if guessesRemaining > 0:
        print(f"You have {guessesRemaining} guesses remaining!")
    else:
        print("That was your last guess!")

if guess == secretNumber:
    print("Good job! You guessed my number!")
else:
    print(f"Sorry, the number I was thinking of was {secretNumber}")
