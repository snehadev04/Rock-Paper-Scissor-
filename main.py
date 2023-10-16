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
game = [ rock , paper , scissors]
print("let's play rock, paper, scissors!")

user_choice = int(input("what is your choice? Type 0 for rock, 1 for paper, or 2 for scissors."))



if (user_choice >= 3) or (user_choice < 0):
  print("its a invalid number")

else:
 print(game[user_choice])

import random

computer_choice = random.randint(0,2)

print("computer chooses:")

print(game[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("you win!")

elif user_choice == 0 and computer_choice == 1:
    print("you lose!")

elif user_choice == 1 and computer_choice == 0:
  print("you win!")
elif user_choice == 1 and computer_choice == 2:
  print("you loose!")

elif user_choice == 2 and computer_choice == 1:
  print("you win!")

elif user_choice == 2 and computer_choice == 0:
  print("you lose!")

elif computer_choice == user_choice:
  print("it's a tie!")
else:
  print("invalid choice")
  #this can also be done in other ways
#print("let's play rock, paper, scissors!")

#user_choice = int(input("what is your choice? Type 0 for rock, 1 for paper, or 2 for scissors."))

#if user_choice == 0:

  #print("rock")

#elif user_choice == 1:

  #print("paper")

#elif user_choice == 2:

  #print("scissors")

 

#elif(user_choice >= 3) and (user_choice < 0):

  #print("its a invalid number")

#else:

  #print("its a invalid number")

 

#import random

#computer_choice = random.randint(0,2)

#print("computer chooses:")

#if computer_choice == 0:

  #print("rock")

#elif computer_choice == 1:

 # print("paper")

#else:

  #print("scissors")

#if (user_choice == 0 and computer_choice == 2) or(user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):

  #print("you win!")

#elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):

  #print("you lose!")

 

#elif computer_choice == user_choice:

  #print("it's a tie!")

#else:

  #print("invalid choice")

