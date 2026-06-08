import random
fruits = ["apple", "banana", "mango", "orange", "grapes"]
word = random.choice(fruits)
guessed_word = ["_"] * len(word)
guessed_letters = []
chances = 6
print("Welcome to Fruit Hangman!")
while chances > 0:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

        print("Correct!")
    else:
        chances -= 1
        print("Wrong!")
        print("Remaining chances:", chances)
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You Won!")
        print("Fruit:", word)
        break
if chances == 0:
    print("\n Game Over!")
    print("The fruit was:", word)