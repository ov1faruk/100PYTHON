import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list_length=len(names)
random_index=random.randint(0,list_length-1)
random_name=names[random_index]
print(f"{random_name} is going to buy the meal today!")