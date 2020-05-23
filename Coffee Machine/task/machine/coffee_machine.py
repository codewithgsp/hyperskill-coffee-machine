# Write your code here
# initial resources
water_qty = 400
milk_qty = 540
coffee_beans_qty = 120
disposable_cup_qty = 9
total_amount = 550


def machine_display(water_, milk_, beans_, cups_, amount_):
    print('''The coffee machine has:
    {water_qty} of water
    {milk_qty} of milk
    {coffee_beans_qty} of coffee beans
    {disposable_cups} of disposable cups
    {total_amount} of money
    '''.format(water_qty=water_,
               milk_qty=milk_,
               coffee_beans_qty=beans_,
               disposable_cups=cups_,
               total_amount=amount_))


def calculate_resources(water_, milk_, beans_, cups_, cost_):
    global water_qty, milk_qty, coffee_beans_qty, disposable_cup_qty, total_amount

    if water_qty - water_ < 0:
        print('Sorry, not enough water!')
        return False
    water_qty -= water

    if milk_qty - milk_ < 0:
        print('Sorry, not enough milk!')
        return False
    milk_qty -= milk_

    if coffee_beans_qty - beans_ < 0:
        print('Sorry, not enough beans!')
        return False
    coffee_beans_qty -= beans_

    if disposable_cup_qty - cups_ < 0:
        print('Sorry, not enough cups!')
        return False
    disposable_cup_qty -= cups_
    total_amount += cost_
    print('I have enough resources, making you a coffee!')
    return True


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()

    if action == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        beverage_type = input()
        if beverage_type != 'back':
            cup = 1  # since 1 cup of beverage is always ordered
            if beverage_type == '1':
                water = 250
                beans = 16
                milk = 0
                cost = 4
            elif beverage_type == '2':
                water = 350
                beans = 20
                milk = 75
                cost = 7
            else:
                water = 200
                beans = 12
                milk = 100
                cost = 6
            if not calculate_resources(water, milk, beans, cup, cost):
                continue

    elif action == 'fill':

        print('Write how many ml of water do you want to add:')
        water = int(input())
        water_qty += water

        print('Write how many ml of milk do you want to add:')
        milk = int(input())
        milk_qty += milk

        print('Write how many grams of coffee beans do you want to add:')
        beans = int(input())
        coffee_beans_qty += beans

        print('Write how many disposable cups of coffee do you want to add:')
        cups = int(input())
        disposable_cup_qty += cups

    elif action == 'take':
        amount_given = total_amount
        total_amount -= amount_given
        print('I gave you ${amount}'.format(amount=amount_given))

    elif action == 'remaining':
        machine_display(water_qty, milk_qty, coffee_beans_qty, disposable_cup_qty, total_amount)

    elif action == 'exit':
        break
