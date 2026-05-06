MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_earnings = 0.0
machine_is_running = True

def money_machine(choice):
    if choice == "espresso":
        print(f"Espresso: ${MENU.get('espresso')['cost']}")
    elif choice == "latte":
        print(f"Latte: ${MENU.get('latte')['cost']}")
    elif choice == "cappuccino":
        print(f"Cappuccino: ${MENU.get('cappuccino')['cost']}")
    pennies = float(input("How many pennies? ")) * 0.01
    nickels = float(input("How many nickels? ")) * 0.05
    dimes = float(input("How many dimes? ")) * 0.10
    quarters = float(input("How many quarters? ")) * 0.25
    total_inserted = pennies + nickels + dimes + quarters
    if total_inserted >= MENU[choice]['cost']:
        print(f"Thank you for your purchase! Enjoy your {choice}")
        global total_earnings
        total_earnings += MENU[choice]['cost']
        print(f"Money returned in change: ${total_inserted - MENU[choice]['cost']}")
    else:
        print("Sorry, you don't have enough money! Money refunded.")

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



def coffee_maker():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        global machine_is_running
        machine_is_running = False
    elif choice == "report":
        global total_earnings
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Earnings: ${total_earnings}")
    else:
        calculate_resources(choice)
        money_machine(choice)

