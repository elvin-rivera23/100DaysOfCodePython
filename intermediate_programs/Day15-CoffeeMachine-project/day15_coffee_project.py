# Elvin Rivera
# Created: 7/28/2021

# Make 3 hot flavours
#     have different prices & levels of coffee, water, milk
# Coin operated: penny, nickel, dime, quarter

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

profit = 0  # This will show how much the machine has made when you run the report

# ingredients comes from dictionary key of each Drink Available (e.g. cappuccino)
def enough_resource(order_ingredients):
    """Returns True if there are enough ingredients to make the drink, False if not enough resources."""
    for ingredient in order_ingredients:
        # compare ingredient for ingredient in both dictionaries
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there are not enough {ingredient} to complete your order.")
            return False
    return True


# check how much money they have
def count_coins():
    print("Please insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Return True when payment is accepted, False if money isn't enough.
    :param money_received:, :param drink_cost:, :return:    <-- these are parameters/args you'll have in the function
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)    # round to 2 decimals
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost    # drink_cost comes from MENU (dictionary)
        return True
    else:
        print("Sorry you do not have enough for this. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Make cup and use resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item] # removing order ingredients from resources
    print(f"Here is your {drink_name} ☕️. Enjoy!")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water left: {resources['water']}ml")
        print(f"Milk left: {resources['milk']}ml")
        print(f"Coffee left: {resources['water']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # when you call the function the argument is: enough_resource(dictionary[dictionary_key])
        if enough_resource(drink["ingredients"]):
            payment = count_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


