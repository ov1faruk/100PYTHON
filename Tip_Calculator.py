print("Welcome to the tip calculator!\n")
bill=input("What was the total bill?\n$")
tip=input("How much tip(%) would you like to give?\n")
split=input("How many people to split the bill?\n")

bill_converted=float(bill)
tip_converted=bill_converted*(float(tip)/100)
split_converted=int(split)
pay=(tip_converted+bill_converted)/split_converted
pay="{:.2f}".format(pay)
print(f"Each person should pay ${pay}")
