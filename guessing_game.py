import random

easy_words = ["cat", "dog", "sun", "moon", "tree", "house", "car", "book", "ball", "bird"]
medium_words = ["bicycle", "elephant", "giraffe", "computer", "python", "jazz", "pneumonia", "xylophone", "quizzical", "rhythm"]
hard_words = ["elephant", "giraffe", "computer", "python", "jazz", "pneumonia", "xylophone", "quizzical", "rhythm", "substantial"]

print("Welcome to the Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter difficulty level: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice difficulty level. Defaulting to easy.")
    secret = random.choice(easy_words)

attempts = 0
print("\n guess the word!")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in{attempts} attempts.")
        break
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")
    print("Try again!\n")

