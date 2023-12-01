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
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Invalid choice.")

ai_choice = random.randint(0,2)

if (ai_choice == 0):
  print('Computer chosen:')
  print(rock)
  if (choice == 0):
    print("It's a draw!")
  elif (choice == 1):
    print("You won! Paper has cover the rock!")
  elif (choice == 2):
    print("You lost! Scissors has been broken by the rock!")

if (ai_choice == 1):
  print("Computer chosen:")
  print(paper)
  if (choice == 0):
    print("You lost! Paper has cover the rock!")
  elif (choice == 1):
    print("It's a draw!")
  elif (choice == 2):
    print("You won! Scissors has cut the paper!")

if (ai_choice == 2):
  print("Computer chosen:")
  print(scissors)
  if (choice == 0):
    print("You won! Rock has crushed the scissors!")
  elif (choice == 1):
    print("You lost! Scissors has broken the paper!")
  elif (choice == 2):
    print("It's a draw!")


