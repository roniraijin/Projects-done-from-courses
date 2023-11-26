#this is my attempt at creating a higher or lower game using limited data
#i learned about the global keyword during this which helped me actually complete this project


from game_data import data
from art import vs , logo
import random
num = 0
score = 0
VRG = ''
def person_one():
    num = random.randint(0,49)
    return num
def person_two():
    num = random.randint(0,49)
    return num
score = 0
person_1 = data[person_one()]
person_2 = data[person_two()]
def game():
        global score
        global person_1
        global person_2
        global VRG
        print(logo)
        print(f"Compare A: {person_1['name']} , a {person_1['description']}, from {person_1['country']}.")
        print(vs)
        print(f"Compare B: {person_2['name']} , a {person_2['description']}, from {person_2['country']}")
        VRG = input("Who has more followers? Type 'A' or 'B': ")
        if VRG == 'A':
            if person_1['follower_count'] > person_2['follower_count']:
                score = + 1
                print(f"You're right! Current score: {score}")
                game1()
            elif person_2['follower_count'] > person_1['follower_count']:
                print(f"Sorry, that's wrong. Final score: {score}")
        if VRG == 'B':
            if person_2['follower_count'] > person_1['follower_count']:
                score =+ 1
                print(f"You're right! Current score: {score}")
                game1()
            elif person_1['follower_count'] > person_2['follower_count']:
                print(f"Sorry, that's wrong. Final score: {score}")
def game1():
    global score
    global person_1
    global person_2
    global VRG
    if VRG == 'A':
        person_1 = person_1
        person_2 = person_2 = data[person_two()]
    if VRG == 'B':
        person_1 = person_2
        person_2 = data[person_two()]
    print(f"Compare A: {person_1['name']} , a {person_1['description']}, from {person_1['country']}.")
    print(vs)
    print(f"Compare B: {person_2['name']} , a {person_2['description']}, from {person_2['country']}")
    VRG = input("Who has more followers? Type 'A' or 'B': ")
    if VRG == 'A':
        if person_1['follower_count'] > person_2['follower_count']:
            score = + 1
            print(f"You're right! Current score: {score}")
            game1()
        elif person_2['follower_count'] > person_1['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
    elif VRG == 'B':
        if person_2['follower_count'] > person_1['follower_count']:
            score = + 1
            print(f"You're right! Current score: {score}")
            game1()
        elif person_1['follower_count'] > person_2['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")




game()












