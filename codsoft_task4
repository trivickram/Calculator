
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_score = 0
bot_score = 0

def art(user_art):
    if user_art == "rock":
        print(f"Your choice:\n{rock}\n")
        print(f"Computer choice:\n{bot_choice}")
    elif user_art == "paper":
        print(f"Your choice:\n{paper}\n")
        print(f"Computer choice:\n{bot_choice}")
    elif user_art == "scissors":
        print(f"Your choice:\n{scissors}\n")
        print(f"Computer choice:\n{bot_choice}")
    else:
        print("Enter a valid input!")

def game(user, bot):
    global user_score
    global bot_score

    if user == "rock" and bot == rock or user == "paper" and bot == paper or user == "scissors" and bot == scissors:
        print("It's a draw😎")
    elif user == "rock" and bot == paper:
        print("You lose😖!")
        bot_score += 1
    elif user == "rock" and bot == scissors:
        print("You win🥳!")
        user_score += 1
    elif user == "paper" and bot == scissors:
        print("You lose😖!")
        bot_score += 1
    elif user == "paper" and bot == rock:
        print("You win🥳!")
        user_score += 1
    elif user == "scissors" and bot == rock:
        print("You lose😖!")
        bot_score += 1
    elif user == "scissors" and bot == paper:
        print("You win🥳!")
        user_score += 1
    else:
        print("Something went wrong🤷‍♂️!")

    print(f"Your score: {user_score}")
    print(f"Computer score: {bot_score}")

user_decision = "y"
while user_decision == "y":
    bot_choice = random.choice(game_images)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    art(user_choice)
    game(user_choice, bot_choice)
    user_decision = input("Do you want to continue the game (y/n): ").lower()
    if user_decision != "y" and user_decision != "n":
        print("Enter a valid input!")
