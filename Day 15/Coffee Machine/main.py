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


def coin_checker():
    print("Please insert coins.")
    quarter = float(input("how many quarters?: "))
    dime = float(input("how many dimes?: "))
    nickle = float(input("how many nickles?: "))
    penny = float(input("how many pennies?: "))

    total_amount = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    if total_amount > MENU[choice]["cost"]:
        return_amount = total_amount - MENU[choice]["cost"]
        print(f"Here is ${return_amount} in change.")
        return True
    elif total_amount == MENU[choice]["cost"]:
        return True
    elif total_amount < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")


def resource_manager():
    if choice == 'espresso':
        if resources["water"] > 50 and resources["coffee"] > 18:
            if coin_checker() == True:
                resources["water"] -= 50
                resources["coffee"] -= 18
                resources["Money"] += 1.50
                print("Here is your espresso ☕. Enjoy!")
        else:
            print("Sorry there is not enough water.")
    elif choice == 'latte':
        if resources["water"] > 200 and resources["milk"] > 150 and resources["coffee"] > 24:
            if coin_checker() == True:
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
                resources["Money"] += 2.50
                print("Here is your latte ☕. Enjoy!")
        else:
            print("Sorry there is not enough water.")
    elif choice == 'cappuccino':
        if resources["water"] > 250 and resources["milk"] > 100 and resources["coffee"] > 24:
            if coin_checker() == True:
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
                resources["Money"] += 3.00
                print("Here is your cappuccino ☕. Enjoy!")
        else:
            print("Sorry there is not enough water.")


choice = ''
resources["Money"] = 0

while choice != 'off':
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["Money"]}')
    resource_manager()
