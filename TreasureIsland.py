class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print(color.BOLD+color.GREEN+"WELCOME TO TREASURE ISLAND\n"+color.END)

print(color.BOLD+color.GREEN +
      "your mission is to find the treasure and get to the other side of the island\n"+color.END)

print("you can move left or right\n")

move = input("Choose L or R to move\n")

if move == "L":
    print("you are in front of a river\n")
    print("you can swim or wait\n")
    swim = input("Choose S or W to swim or wait\n")
    if swim == "W":
        print("you are in front of a CASTLE\n")
        print("There are 3 doors: "+color.BOLD+color.RED+" RED"+color.BLUE+" BLUE"+color.YELLOW+" YELLOW\n"+color.END)
        door = input("Choose R, B or Y to open the door\n")
        if door == "Y":
            print(color.BOLD+color.YELLOW+"YOU FOUND THE TREASURE!!!BRAVO!!\n"+color.ENDL)
        elif door == "B":
            print("GAME OVER!!! You are eaten by beasts! :( \n")
        elif door == "R":
            print("GAME OVER!!! You are burned by fire! :( \n")

    else:
        print("you are attacked by TROUT\n")
        print("you are dead\n")

else:
    print("You fell into a hole and died\n")
    print("GAME OVER")
