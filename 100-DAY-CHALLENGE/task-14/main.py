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
    "money": 0
}


def report():
    print(
        f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')


def cost_of_drink(drink):
    return MENU[drink]['cost']


def process_payment(price):
    print('Please insert coins.')
    payment = (int(input("How many quarters?: ")) * 0.25 +
               int(input("How many dimes?: ")) * 0.1 +
               int(input("How many nickels?: ")) * 0.05 +
               int(input("How many pennies?: ")) * 0.01)

    if payment < price:
        print('Sorry, that is not enough money. Money refunded.')
        return False, payment
    else:
        change = payment - price
        resources['money'] += price
        print(f'Here is ${change:.2f} in change.')
        return True, change


while True:
    cust_inp = input('What would you like to order? (latte, espresso, cappuccino): ').lower()

    if cust_inp == 'report':
        report()
    elif cust_inp in MENU:
        # Check if there are enough resources
        drink = MENU[cust_inp]

        if (resources['water'] >= drink['ingredients']['water'] and
                resources['milk'] >= drink['ingredients'].get('milk', 0) and
                resources['coffee'] >= drink['ingredients']['coffee']):

            # Process payment
            price = cost_of_drink(cust_inp)
            success, _ = process_payment(price)

            if success:
                # Deduct ingredients
                resources['water'] -= drink['ingredients']['water']
                resources['milk'] -= drink['ingredients'].get('milk', 0)
                resources['coffee'] -= drink['ingredients']['coffee']
                print(f'Here is your {cust_inp} ☕️. Enjoy!')

        else:
            if resources['water'] < drink['ingredients']['water']:
                print('Sorry, not enough water.')
            if resources['milk'] < drink['ingredients'].get('milk', 0):
                print('Sorry, not enough milk.')
            if resources['coffee'] < drink['ingredients']['coffee']:
                print('Sorry, not enough coffee.')

    elif cust_inp == 'off':
        print('Turning off...')
        break