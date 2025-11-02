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
choose_ind = [rock,paper,scissors]
choice = int(input("what do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))

if choice >= 0 and choice <= 2:
    print(choose_ind[choice])
computer = random.randint(0,2)
print("Computer chose: ")
print(choose_ind[computer])

if choice == 0:
   if computer == 1:
       print("Computer wins")
   if computer == 2:
       print("You wins")
elif choice == 1:
    if computer == 0:
        print("You wins")
    if computer == 2:
        print("Computer wins")
elif choice == 2:
    if computer == 0:
        print("Computer wins")
    if computer == 1:
        print("You wins")
else:
    print("wrong output")


    
    
