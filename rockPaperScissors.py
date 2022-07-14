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
images=[rock,paper,scissors]

choice=int(input("0:Rock?\n1:Papers?\n2:Scissors?\nType 0 or 1 or 2\n"))
if choice<0 or choice>2:
    print("Invalid choice")
else:
    print(f"you chose:"+images[int(choice)])



    randChoice=random.randint(0,2)

    
    if choice==randChoice:
        print(randChoice)
        print(f"The computer chose:"+images[randChoice])
        print("Draw")
    elif choice==0 and randChoice==1:
        print(f"The computer chose:"+images[randChoice])
        print("You Loose")
    elif choice==0 and randChoice==2:
        print(f"The computer chose:"+images[randChoice])
        print("You WIN")
    elif choice==1 and randChoice==0:
        print(f"The computer chose:"+images[randChoice])
        print("YOU WIN")
    elif choice==1 and randChoice==2:
        print(f"The computer chose:"+images[randChoice])
        print("YOU LOOSE")
    elif choice==2 and randChoice==0:
        print(f"The computer chose:"+images[randChoice])
        print("YOU LOOSE")
    elif choice==2 and randChoice==1:
        print(f"The computer chose:"+images[randChoice])
        print("YOU WIN")
    else:
        print("Error")
        print(f"The computer chose:"+images[randChoice])
        print("YOU LOOSE")
    

