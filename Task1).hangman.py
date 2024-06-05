import random

def choose_word():
    words=['python','programming','hangman','code','game']
    return random.choice(words)

def display_word(word, guessed_letter):
    display = ''
    for letter in word:
        if letter in guessed_letter:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempt = 6

    print("Welcome to Hangman")
    print("Guess the word")

    while True:
        print("\nAttempt left:",attempt)
        print("Word:",display_word(word,guessed_letters))

        if '_' not in display_word(word,guessed_letters):
            print("Congratulations! you've guessed the wcord:",word)
            break
        if attempt == 0:
            print("sorry,you run out of attempt.The word was:",word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("please enter a single letter")
            continue

        if guess in guessed_letters:
            print("you've already guessed that letters")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempt = -1
            print("Incorrect guess!")
hangman()