print("Welcome to the tip calculator")
cost = input("Enter cost of service: ")
tip = float(cost) * 0.15
print("Your tip amount is:", round(tip, 2))
print(f"The total cost is {round(tip + float(cost), 2)}")