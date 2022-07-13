print("###############################\n")
print("Welcome to the Love Calculator!\n")

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

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name=name1+name2
name=name.lower()

L=name.count("l")
O=name.count("o")
V=name.count("v")
E=name.count("e")

love=L+O+V+E

T=name.count("t")
R=name.count("r")
U=name.count("u") 
E=name.count("e") 

true=T+R+U+E

score=f"{true}{love}"
score=int(score)
if score<10 or score>90:
    print(f"your score is {score},"+color.BOLD+"you go together like "+color.RED+"coke "+color.END+"and"+color.BLUE+" mentos."+color.END)
elif score>40 and score<50:
    print(f"your score is {score},"+color.BOLD+"you are alright together."+color.END)
else:
    print(f"your score is {score}")
