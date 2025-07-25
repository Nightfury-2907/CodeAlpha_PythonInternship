import random

words_easy = ["apple", "mouse", "delta", "chair", "glass"]
words_medium = ["python", "laptop", "random", "planet", "guitar"]
words_hard = ["encyclopedia", "javascript", "mysterious", "microbiology", "configuration"]

def choose_difficulty():
    print("Select Difficulty:")
    print("1. Easy (5-letter words)")
    print("2. Medium (6-8 letter words)")
    print("3. Hard (9+ letter words)") 

    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            return random.choice(words_easy)
        elif choice == '2':
            return random.choice(words_medium)
        elif choice == '3':
            return random.choice(words_hard)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def display_state(guessed_word, used_letters, lives):
    print("\nWord: " + " ".join(guessed_word))
    print("Used Letters:", ", ".join(sorted(used_letters)))
    print("Lives Left:", lives)

def play_game():
    print("🎮 Welcome to Advanced Hangman!")
    print("Guess the word one letter at a time. You have 6 chances.")

    word = choose_difficulty().lower()
    guessed = ["_"] * len(word)
    used = set()
    lives = 6

    while lives > 0 and "_" in guessed:
        display_state(guessed, used, lives)
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetic character.")
            continue

        if guess in used:
            print("⚠️ You already guessed that letter!")
            continue

        used.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("✅ Correct!")
        else:
            lives -= 1
            print("❌ Wrong guess!")

    if "_" not in guessed:
        print("\n🎉 You win! The word was:", word)
    else:
        print("\n💀 You lost! The word was:", word)

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Thanks for playing Hangman! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
