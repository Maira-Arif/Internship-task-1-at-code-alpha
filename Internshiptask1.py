import random

words = ["python", "coding", "laptop", "internet", "program"]
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    if "_" not in display:
        print("You won! 🎉")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        wrong += 1
        print("Wrong! Chances left:", max_wrong - wrong)
else:
    print("You lost! The word was:", word)