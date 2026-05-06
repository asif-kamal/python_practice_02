import resources as res
import money_machine as money
import main


def coffee_maker():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        main.machine_is_running = False
    elif choice == "report":
        print(f"Water: {res.resources['water']}")
        print(f"Milk: {res.resources['milk']}")
        print(f"Coffee: {res.resources['coffee']}")
        print(f"Earnings: ${money.total_earnings}")
    else:
        res.calculate_resources(choice)
        money.money_machine(choice)

