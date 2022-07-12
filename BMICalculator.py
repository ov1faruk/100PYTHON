import math

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

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
   
bmi=weight/height**2
bmi=math.ceil(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, "+color.BOLD + color.RED+"you are underwight."+color.END)
elif bmi <=25:
    print(f"Your BMI is {bmi}, "+color.BOLD +color.GREEN+ "you are normal weight."+color.END)
elif bmi<=30:
    print(f"Your BMI is {bmi}, "+color.BOLD +color.YELLOW+ "you are slightly overweight."+color.END)
elif bmi<=35:
    print(f"Your BMI is {bmi}, " +color.BOLD +color.PURPLE+ "you are obese."+color.END)
else:
    print(f"Your BMI is {bmi}, "+color.BOLD +color.RED+color.UNDERLINE+ "you are clinically obese."+color.END)