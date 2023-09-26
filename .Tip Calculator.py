
print("Welcom to the Tip Calculator")
bill = input("What was the totall bill? PLN")
tip = input("What percentage tip do you want to give - 10, 12 or 15? ")
split = input("How many people to split the bill? ")
bill = float(bill)
tip = int(tip)
split = int(split)
tip_percentage = tip/100
bill_plus = bill * tip_percentage
bill_end = bill + bill_plus
spliting = round(bill_end/split,2)
spliting ="{:.2f}".format(spliting)
print(f"You need to pay PLN: {spliting} for person")