# this is the new class
class CoffeeMachine:

    # class instance, as these should be shared for each instance
    water_qty = 400
    milk_qty = 540
    coffee_beans_qty = 120
    dispo_cup_qty = 9
    total_money = 550

    def determine_action(self, action):
        if action == 'remaining':
            self.remaining(CoffeeMachine.water_qty,
                           CoffeeMachine.milk_qty,
                           CoffeeMachine.coffee_beans_qty,
                           CoffeeMachine.dispo_cup_qty,
                           CoffeeMachine.total_money)
        elif action == 'take':
            self.take()

        elif action == 'fill':
            self.fill()

        elif action == 'buy':
            print(self.buy())

    def remaining(self, water, milk, coffee_beans, dispo_cup, money):
        print('The coffee machine has:\n'
              '{} of water\n{} of milk\n'
              '{} of coffee beans\n'
              '{} of disposable cups\n'
              '${} of money'.format(water, milk, coffee_beans, dispo_cup, money))

    def take(self):
        amount_given = CoffeeMachine.total_money
        CoffeeMachine.total_money -= amount_given
        print('I gave you ${}'.format(amount_given))

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        beverage_type = input()
        if beverage_type != 'back':
            cup = 1  # since 1 cup of beverage is always ordered
            if beverage_type == '1':
                water, beans, milk, cost = 250, 16, 0, 4
            elif beverage_type == '2':
                water, beans, milk, cost = 350, 20, 75, 7
            elif beverage_type == '3':
                water, beans, milk, cost = 200, 12, 100, 6

            # calculate resources before making a coffee
            return self.calculate_resources(water, milk, beans, cup, cost)
        return None

    def fill(self):
        print('Write how many ml of water do you want to add:')
        CoffeeMachine.water_qty += int(input())

        print('Write how many ml of milk do you want to add:')
        CoffeeMachine.milk_qty += int(input())

        print('Write how many grams of coffee beans do you want to add:')
        CoffeeMachine.coffee_beans_qty += int(input())

        print('Write how many disposable cups of coffee do you want to add:')
        CoffeeMachine.dispo_cup_qty += int(input())

    def calculate_resources(self, water_, milk_, beans_, cup_, cost_):
        if CoffeeMachine.water_qty - water_ < 0:
            return 'Sorry, not enough water!'
        CoffeeMachine.water_qty -= water_

        if CoffeeMachine.milk_qty - milk_ < 0:
            return 'Sorry, not enough milk!'
        CoffeeMachine.milk_qty -= milk_

        if CoffeeMachine.coffee_beans_qty - beans_ < 0:
            return 'Sorry, not enough beans!'
        CoffeeMachine.coffee_beans_qty -= beans_

        if CoffeeMachine.dispo_cup_qty - cup_ < 0:
            return 'Sorry, not enough cups!'
        CoffeeMachine.dispo_cup_qty -= cup_

        CoffeeMachine.total_money += cost_
        return 'I have enough resources, making you a coffee!'


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    response = input()
    if response == 'exit':
        break
    coffee_machine = CoffeeMachine()
    coffee_machine.determine_action(response)
