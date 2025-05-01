import random

def hangman():
    # Step 1: Define a list of words.
    # We have a list of words from which one will be picked randomly.
    words = ['python', 'programming', 'hangman', 'challenge', 'openai']
    
    # Step 2: Choose one word randomly.
    chosen_word = random.choice(words)
    
    # This list will hold every letter that the player guesses.
    guessed_letters = []
    
    # The number of tries (chances) the player has.
    tries = 6

    print("Welcome to Hangman!")
    print("Guess the word letter by letter.")

    # Step 3: The game loop.
    # This loop runs while the player still has tries left.
    while tries > 0:
        # Build the word display: show the letter if guessed, else show an underscore.
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord:", display_word)

        # Check if the player has guessed all the letters.
        if "_" not in display_word:
            print("Congratulations! You've guessed the word!")
            break

        # Ask the player to guess a letter.
        guess = input("Enter a letter: ").lower()

        # Step 4: Validate the input.
        # If the input is not just one letter, tell the player and continue to the next loop.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # If the letter has already been guessed, remind the player.
        if guess in guessed_letters:
            print("You already guessed that letter!", guess)
            continue

        # Add the new letter to our list of guessed letters.
        guessed_letters.append(guess)

        # Step 5: Check if the guessed letter is in the chosen word.
        if guess not in chosen_word:
            tries -= 1
            print("Oops! That letter is not in the word.")
            print("Tries left:", tries)
        else:
            print("Nice! That letter is in the word.")

    # Step 6: If the loop ends and tries are 0, the player loses.
    if tries == 0:
        print("\nSorry, you ran out of tries. The word was:", chosen_word)

# Start the hangman game.
hangman()
