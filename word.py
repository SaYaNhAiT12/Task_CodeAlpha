import random

def hangman():
    
    words = ["python", "hangman", "random", "simple", "coding"]
    word = random.choice(words)  
    guessed_word = ["_"] * len(word)  
    guessed_letters = []  
    attempts = 6  

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(" ".join(guessed_word))
    print(f"You have {attempts} incorrect attempts allowed.\n")

    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            print(f"Remaining attempts: {attempts}")

        print(" ".join(guessed_word))
        print()

    
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
