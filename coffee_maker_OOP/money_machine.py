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

total_earnings = 0.0

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