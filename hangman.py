#project from course but heavywork was done by myself
import random , hangman_words , hangman_art
from replit import clear
word_list = hangman_words.word_list
stages = hangman_art.stages
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
bob = ''
bob = list(bob)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
  
    if guess in bob:
          print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            bob += guess
        
    
          
         
          #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry, {guess} is incorrect.")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
