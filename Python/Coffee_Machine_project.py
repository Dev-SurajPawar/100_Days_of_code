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
profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins: ")
    total = int(input("Hom many quarters? ")) * 0.25
    total += int(input("Hom many dimes? ")) * 0.1
    total += int(input("Hom many nickles? ")) * 0.05
    total += int(input("Hom many pennies? ")) * 0.01
    return total


def is_transaction_Successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


is_on = True
while is_on:
    user_req = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_req == "off":
        is_on = False
    elif user_req == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[user_req]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_Successful(payment, drink["cost"]):
                make_coffee(user_req, drink["ingredients"])
