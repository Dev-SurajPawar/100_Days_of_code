import random
from Hangman_Stages import stages
from Hangman_Words import word_list

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(f"Chosen Word: {chosen_word}")

display = []
for _ in chosen_word:
    display.append("_")

while not end_of_game:

    guess = input("Guess a Letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose life")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You Lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])