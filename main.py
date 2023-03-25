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

#Write your code below this line 👇
game_images =[rock,paper,scissors]
user_chose = int(input("What do you chose? Type 0 for rock ,1 for paper, 2 for scissors .\n"))
print(game_images[user_chose])
computer_chose = random.randint(0,2)
print("computer_chose")
print(game_images[computer_chose])
if user_chose == 0 and computer_chose == 2:
  print("you win")
elif user_chose == 0 and computer_chose ==1:
  print("you lose")
elif user_chose == 0 and computer_chose == 0:
  print("it's draw")
elif  user_chose == 1 and computer_chose == 0: 
  print("You win")
elif  user_chose == 1 and computer_chose == 2:  
  print("you lose")
elif user_chose == 1 and computer_chose == 1:
  print("It's draw")
elif user_chose == 2 and computer_chose == 1:
  print("you win")
elif user_chose == 2 and computer_chose ==0:
  print("you lose")
elif user_chose == 2 and computer_chose == 2:
  print("it's draw")  