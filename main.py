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
    "money": 1,
}

coin_values = {
    'Quarters': 0.25,
    'Dimes': 0.1,
    'Nickels': 0.05,
    'Pennies': 0.01
}

coin_types = ['Quarters', 'Dimes', 'Nickels', 'Pennies']

user_choice = input("What would you like? (espresso/latte/cappuccino): ")


def coin_counter():
    coin_counts = {}
    # For loop that asks how many coins the user has from the coin_values dictionary
    for coin_type in coin_types:
        count = int(input(f"How many {coin_type}?: "))
        coin_counts[coin_type] = count

    return coin_counts


def coins_to_dollars(coin_counts=None):
    total_dollars = 0
    # For loop that converts the coin types to dollars
    for coin_type, count in coin_counts.items():
        total_dollars += count * coin_values[coin_type]  # Now, total_dollars contains the total value in dollars.

    return total_dollars


# Now make a program for each coffee choice that gives coffee, checks resources and returns the change

if user_choice == "espresso":
    if total_dollars < MENU["espresso"]["cost"]:
        print("Sorry that is not enough money. Money refunded")
    else:
        coin_counter()
        coins_to_dollars()
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU["espresso"]["cost"]
        change_returned = total_dollars - MENU["espresso"]["cost"]

        print("Here is your espresso")
        print(f"Keep the change, motherfucker: {change_returned:.2f}$")

if user_choice == "latte":
    if total_dollars < MENU["latte"]["cost"]:
        print("Sorry that is not enough money. Money refunded")
    else:
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["money"] = resources["money"] + MENU["latte"]["cost"]
        change_returned = total_dollars - MENU["latte"]["cost"]

        print("Here is your latte")
        print(f"Keep the change, motherfucker: {change_returned:.2f}$")

if user_choice == "cappuccino":
    if total_dollars < MENU["latte"]["cost"]:
        print("Sorry that is not enough money. Money refunded")
    else:
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["money"] = resources["money"] + MENU["cappuccino"]["cost"]
        change_returned = total_dollars - MENU["latte"]["cost"]

        print("Here is your latte")
        print(f"Keep the change, motherfucker: {change_returned:.2f}$")

if user_choice == "report":
    for value in resources.values():
        print(value)

        # Push test https://www.youtube.com/watch?v=8ZEssR8VTKo#

        #Pull git branch