# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=name1+name2
name=name.lower()
# print(name)
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
    print(f"your score is {score},you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"your score is {score},you are alright together.")
else:
    print(f"your score is {score}")