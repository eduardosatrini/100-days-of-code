import data

is_on = True
profit = 0
msg = "What Would you like? (espresso/latte/cappuccino): "

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= data.resources[item]:
           print(f"Sorry there is not enough {item}")
           return False

    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    return total


def is_transaction_successul(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"{money_received} Sorry that's not enough money..", end="")
        print(" Money refunded.")
        return False 

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name}")
    

while is_on:
    option = str(input(msg)).strip().lower()

    if option == "off":
        is_on = False
    elif option == "report":
        print(f"> water:  {data.resources['water']}ml")
        print(f"> milk:   {data.resources['milk']}ml")
        print(f"> coffee: {data.resources['coffee']}mg")
        print(f"> money:  {profit}")
    else:
        drink = data.MENU[option]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()           
            if is_transaction_successul(payment, drink["cost"]):
                make_coffee(option, drink["ingredients"])






