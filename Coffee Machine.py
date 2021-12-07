current_water = 400
current_milk = 540
current_beans = 120
current_money = 550
current_cups = 9
switch_off = True


def current_print():
    print("The coffee machine has:")
    print(current_water, "of water")
    print(current_milk, "of milk")
    print(current_beans, "of coffee beans")
    print(current_cups, "of disposable cups")
    print(current_money, "of money")


def action():
    global current_water
    global current_beans
    global current_money
    global current_cups
    global current_milk
    global switch_off
    wanted_action = input("Write action (buy, fill, take, remaining, exit):")
    if wanted_action == "buy":
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "1":
            if current_water < 250:
                print("Sorry, not enough water!")
            elif current_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif current_cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                current_water -= 250
                current_beans -= 16
                current_money += 4
                current_cups -= 1
        elif coffee_type == "2":
            if current_water < 350:
                print("Sorry, not enough water!")
            elif current_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif current_cups < 1:
                print("Sorry, not enough disposable cups!")
            elif current_milk < 75:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                current_water -= 350
                current_beans -= 20
                current_money += 7
                current_cups -= 1
                current_milk -= 75
        elif coffee_type == "3":
            if current_water < 200:
                print("Sorry, not enough water!")
            elif current_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif current_cups < 1:
                print("Sorry, not enough disposable cups!")
            elif current_milk < 100:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                current_water -= 200
                current_beans -= 12
                current_money += 6
                current_cups -= 1
                current_milk -= 100
    elif wanted_action == "fill":
        add_water = int(input("Write how many ml of water you want to add:"))
        add_milk = int(input("Write how many ml of milk you want to add:"))
        add_beans = int(input("Write how many grams of coffee beans you want to add:"))
        add_cups = int(input("Write how many disposable coffee cups you want to add:"))
        current_water += add_water
        current_beans += add_beans
        current_cups += add_cups
        current_milk += add_milk
        current_print()
    elif wanted_action == "remaining":
        current_print()
    elif wanted_action == "take":
        print("I gave you $", current_money, sep="")
        current_money = 0
        current_print()
    else:
        switch_off = False


while switch_off == True:
    action()
