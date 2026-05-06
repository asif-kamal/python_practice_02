resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculate_resources(choice):
    if choice == "espresso":
        if resources["water"] > 49:
            if resources["coffee"] > 17:
                resources["water"] -= 50
                resources["coffee"] -= 18
            else:
                print(f"Sorry, we don't have enough coffee")
        else:
            print(f"Sorry, we don't have enough water")
    elif choice == "latte":
        if resources["milk"] > 149:
            if resources["coffee"] > 23:
                if resources["water"] > 199:
                    resources["milk"] -= 100
                    resources["coffee"] -= 24
                    resources["water"] -= 250
                else:
                    print(f"Sorry, we don't have enough water")
            else:
                print(f"Sorry, we don't have enough coffee")
        else:
            print(f"Sorry, we don't have enough milk")
    elif choice == "cappuccino":
        if resources["milk"] > 99:
            if resources["coffee"] > 23:
                if resources["water"] > 249:
                    resources["milk"] -= 150
                    resources["coffee"] -= 24
                    resources["water"] -= 200
                else:
                    print(f"Sorry, we don't have enough water")
            else:
                print(f"Sorry, we don't have enough coffee")
        else:
            print(f"Sorry, we don't have enough milk")
