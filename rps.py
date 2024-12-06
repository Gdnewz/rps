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
game_start = input("What do you choose? "
      "Type 0 for Rock, 1 for paper "
      "or 2 for scissors\n")

if game_start == '0':
    print(rock)

elif game_start == '1':
    print(paper)

elif game_start == '2':
    print(scissors)

else:
    print("Please choose between "
          "the required numbers")

computer_game =[rock, paper, scissors]
choice = random.choice(computer_game)
print("Computer chose:{0}".format(choice))
# game_index = random.randint(0, 2)
# computer_chose = computer_game[game_index]
# print("Computer chose:{0}".format(computer_chose))
#
if game_start == '0' and choice == scissors :
     print("YOU WIN! ROCK BEATS SCISSORS.")

elif game_start == '2' and choice == paper :
     print("You Win! Scissors beats paper.")

elif game_start == '1' and choice == rock:
     print("You Win! Paper beats rock.")

elif choice == rock and game_start == '2':
     print("You Lose! ROCK BEATS SCISSORS.Try Harder")

elif choice == scissors == 2 and game_start =='1':
     print("You Lose! Scissors beats paper.Try Harder")

elif choice == paper  and game_start == '0':
     print("You Lose! Paper beats rock.Try Harder")

else:
    print("IT IS A DRAW")
