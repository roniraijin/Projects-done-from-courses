
yoo = """

  /$$$$$$                                                                                                 /$$                                
 /$$__  $$                                                                                               | $$                                
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$        /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$       
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/       |____  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$      
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         /$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/      
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$       /$$__  $$      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$            
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/      |  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$            
 \______/  \______/  \_______/|_______/|_______/        \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/            
                                                                                                                                             
                                                                                                                                             
                                                                                                                                             

"""
import random
def easy():
  print(yoo)
  lives = 10
  while lives > 0:
    print(f"You have {lives} attempts reminaining to guess the number.")
    the_guess = int(input("Make a guess: "))
    if the_guess == random_number:
      print(f"You got it! The answer was {random_number}")
    else:
      if the_guess > random_number:
        print("Too high.")
      else:
        print("Too low.")
      lives -= 1
  if lives == 0:
    print(f"""You've run out of guesses, you lose. 
    The answer was {random_number}""")
def hard():
  print(yoo)
  lives = 5
  while lives > 0:
    print(f"You have {lives} attempts reminaining to guess the number.")
    the_guess = int(input("Make a guess: "))
    if the_guess == random_number:
      print(f"You got it! The answer was {random_number}")
    else:
      if the_guess > random_number:
        print("Too high.")
      else:
        print("Too low.")
      lives -= 1
  
  if lives == 0:
    print(f"""You've run out of guesses, you lose.
          The answer was {random_number}""")

random_number = random.randint(1,100)
difficulty_level = input("""Welcome to the Number Guessing Game!,
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or hard': """).lower()
if difficulty_level == 'easy':
  print("You've chose the easy mode.")
  easy()
elif difficulty_level == 'hard':
  print("You've chosen the hard mode.")
  hard()
