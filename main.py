# Hangman

import random

player_lives = 10 

words = [
    "confess",
    "vegetable",
    "boiling",
    "drown",
    "stranger",
    "vagabond",
    "sail",
    "quill",
    "linen",
    "influence",
    "creature",
    "spade",
    "longing",
    "kneel",
    "moon",
    "cars",
    "bad",
    "damaged",
    "shame",
    "size",
    "hand",
    "obeisant",
    "decide",
    "voiceless",
    "glamorous",
    "habitual",
    "son",
    "label",
    "planes",
    "bird",
    "hat",
    "position",
    "owe",
    "bit",
    "pushy",
    "scold",
    "unit",
    "pleasant",
    "badge",
    "road",
    "paper",
    "giant",
    "tease",
    "political",
    "identify",
    "dependent",
    "press",
    "puffy",
    "fast",
    "tranquil",
    "best",
    "chilly",
    "resonant",
    "familiar",
    "old",
    "knot",
    "nondescript",
    "breezy",
    "inconclusive",
    "finicky",
    "scribble",
    "majestic",
    "defiant",
    "accidental",
    "stay",
    "mellow",
    "cat",
    "evasive",
    "brief",
    "increase",
    "snobbish",
    "grateful",
    "dinosaurs",
    "upbeat",
    "want",
    "righteous",
    "magenta",
    "cultured",
    "inquisitive",
    "frail",
    "grotesque",
    "wait",
    "unusual",
    "money",
    "consider",
    "exercise",
    "lumpy",
    "earsplitting",
    "childlike",
    "cooperative",
    "simplistic",
    "white",
    "unruly",
    "sugar",
    "touch",
    "swim",
    "wooden",
    "hurt",
    "real",
]

# Select a random word from the list of words and convert it to a list using a random int 
word = list(words[random.randint(0, len(words) -1)])

# Create a list that is the length of our selected word
word_length = list(range(len(word)))

# Create an empty list where we will add our hints and also record sucsesfull guesses as to compre agaisnt the main word
word_hint = []

# Fill our word_hint list by creating a list the length of our origonal word with blank entries
for i in word_length:
    word_hint.append("-")

# Use our main word list and generate a string from it for string comparison later
word_as_string = ("".join(word))

print("Welcome to hangman!")

while player_lives > 0:

    # Convert our word hint list to a string this will be rebuilt on every itteration to show all current correct guesses and blank spaces still to guess
    word_hint_as_string = ("".join(word_hint))

    # Logic to test if the string of our word is equal to the string of the word_hint, if so end the game
    if word_as_string == word_hint_as_string:
        print(f"You win with {player_lives} lives remaining")
        break

    print("------------------------------------")
    print(f"Your hint:\n|{word_hint_as_string}|")
    print(f"You have {player_lives} lives remaining")

    player_guess = input("Please guess a letter: ")

    # An empty list to host the indexes a sucsesfull guess exists at
    letter_indexes = []

    # Itterate thought every index in word length
    for index in word_length:
        # If the player guess matches the value at an index append that index to letter_indexes
        if player_guess == word[index]:
            letter_indexes.append(index)
    
    # Itterate through every item in letter_indexes and change the value at that index to be the players guess in word_hint
    for index in letter_indexes:
        word_hint[index] = player_guess

    if player_guess not in word_as_string:
        player_lives -= 1

if player_lives < 1:
    print(f'Game over! The correct word was "{word_as_string}"!')









