from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machiine = MoneyMachine()
menu = Menu()
i = 1

while i != 0:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        i = 1

    elif choice == "report":
        coffee_maker.report()
        money_machiine.report()
    
    else:
        drink = menu.find_drink(choice)
        if money_machiine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
                coffee_maker.make_coffee(drink)
