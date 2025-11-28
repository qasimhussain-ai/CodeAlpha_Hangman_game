import random

words = ["python", "apple", "orange", "laptop", "coding"]
word = random.choice(words)
display = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("=== Hangman Game ===")

while attempts > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Attempts left:", attempts)
    
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue
    
    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

if "_" not in display:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n❌ You lost. The word was:", word)
