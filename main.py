#Hangman Python Project
import random

from hangman_words import word_list
chosen_word = random.choice(word_list)

lives = 6

from hangman_art import logo
print(logo)
print(f"The solution is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a Character: ").lower()
   # if clearing the screen after each iteration write code here

    if guess in display:
        print(f"You've already guessed the letter: {guess}")

    for position in range(word_length):
        chr = chosen_word[position]

        # print statement for debugging purpose
        # print(f"Current Position: {position} \nCurrent Character: {chr} \nGuessed Letter: {guess}")
        if chr == guess:
            display[position] = chr

    if guess not in (chosen_word):
        print(f"You guessed {guess}, that's not in the word! you loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    from hangman_art import stages
    print(stages[lives])