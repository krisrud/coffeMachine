class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    money = 550
    cups = 9
    state = "idle"
    output = "Write action (buy, fill, take, remaining, exit):"

    def buy_coffee(self, act):
        if act == "1":
            if self.check_resourse(250, 16, 1, 0):
                self.deal(250, 16, 1, 0, 4)
        elif act == "2":
            if self.check_resourse(350, 20, 1, 75):
                self.deal(350, 20, 1, 75, 7)
        elif act == "3":
            if self.check_resourse(200, 12, 1, 100):
                self.deal(200, 12, 1, 100, 6)
        self.state = "idle"

    def check_resourse(self, water, beans, cups, milk):
        if self.water < water:
            print("Sorry, not enough water!")
            return False
        if self.beans < beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups < cups:
            print("Sorry, not enough disposable cups!")
            return False
        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False
        return True

    def deal(self, water, beans, cups, milk, money):
        print("I have enough resources, making you a coffee!")
        self.water -= water
        self.beans -= beans
        self.milk -= milk
        self.cups -= cups
        self.money += money

    def adding_water(self, act):
        self.water += int(act)
        self.state = "adding_milk"

    def adding_milk(self, act):
        self.milk += int(act)
        self.state = "adding_beans"

    def adding_beans(self, act):
        self.beans += int(act)
        self.state = "adding_cups"

    def adding_cups(self, act):
        self.cups += int(act)
        self.state = "idle"

    def current_print(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")

    def take_money(self):
        print("I gave you $", self.money, sep="")
        self.money = 0

    def do_action(self, act):
        if self.state == "idle":
            if act == "buy":
                self.state = "buying"
                self.output = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
            elif act == "fill":
                self.state = "adding_water"
                self.output = "Write how many ml of water do you want to add:"
            elif act == "remaining":
                self.current_print()
            elif act == "take":
                self.take_money()
        elif self.state == "buying":
            self.buy_coffee(act)
            self.output = "Write action (buy, fill, take, remaining, exit):"
        elif self.state == "adding_water":
            self.adding_water(act)
            self.output = "Write how many ml of milk do you want to add:"
        elif self.state == "adding_milk":
            self.adding_milk(act)
            self.output = "Write how many grams of coffee beans do you want to add:"
        elif self.state == "adding_beans":
            self.adding_beans(act)
            self.output = "Write how many disposable cups of coffee do you want to add:"
        elif self.state == "adding_cups":
            self.adding_cups(act)
            self.output = "Write action (buy, fill, take, remaining, exit):"

my_coffee_machine = CoffeeMachine()
while True:
    user_action = input(my_coffee_machine.output)
    if user_action == "exit":
        break
    my_coffee_machine.do_action(user_action)
