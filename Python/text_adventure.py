start = "Welcome to Mall of America! You have a big day of shopping ahead of you. But keep in mind, you only have $125 in your wallet. As soon as you walk in, you walk past Lord & Taylor and spot a dress that you love. The price tag reads $50. Would you like to buy it?"
shoe_message = "You walk out of Lord & Taylor and spot an amazing pair of heels in the display of Macy's, and they're only $40! Do you want to buy them? Type 'kickin!' to buy the shoes or 'no shoes' to pass"
bag_message = "You leave Macy's and walk around the mall for a bit when you decide to enter Nordstrom. You go the sale section and find a designer bag at the low price of $30!!! Would you like to buy it?"
food_message = "All this shopping is making you kind of hungry. You stroll through the food court an eye a $10 combo at taco bell. Hungry for tacos?"
money = 125
print(start)
user_input = input("Type 'yes to the dress' to buy it or 'no dress' to keep looking.")
while user_input != "yes to the dress" and user_input != "no dress":
    print("Type 'yes to the dress' to buy it or 'no dress' to keep looking.")
    user_input = input()
if user_input == "yes to the dress":
    print("You're gonna look great in this dress!") # finished the story by writing what happens
    money = money - 50
    user_input = input(shoe_message)
    while user_input != "kickin!" and user_input != "no shoes":
        print("Type 'kickin!' to buy them or 'no shoes' to pass.")
        user_input = input()
    if user_input == "kickin!":
        money = money - 40
        print(bag_message)
        while user_input != "totes!" and user_input != "no":
            print("Type 'totes!' to buy it or 'no' to keep looking.")
            user_input = input()
        if user_input == "totes!":
            money = money - 30
        elif user_input == "no":
            print("You have plenty of bags at home anyways")
    elif user_input == "no shoes":
        print("That's alright, heels hurt your feet anyways.")
        print(bag_message)
        while user_input != "totes!" and user_input != "no":
            print("Type 'totes!' to buy it or 'no' to keep looking.")
            user_input = input()
        if user_input == "totes!":
            money = money - 30
        elif user_input == "no":
            print("You have plenty of bags at home anyways")
elif user_input == "no dress":
    print("It's okay, you'll find something soon enough") # finished the story writing what happens
    print(shoe_message)
    while user_input != "kickin!" and user_input != "no shoes":
        print("Type 'kickin!' to buy them or 'no shoes' to pass.")
        user_input = input()
    if user_input == "kickin!":
        money = money - 40
        print(bag_message)
        user_input = input("Type 'totes!' to buy the bag or 'no' to pass")
        while user_input != "totes!" and user_input != "no":
            print("Type 'totes!' to buy it or 'no' to keep looking.")
            user_input = input()
        if user_input == "totes!":
            money = money - 30
        elif user_input == "no":
            print("You have plenty of bags at home anyways")
    elif user_input == "no shoes":
        print("That's alright, heels hurt your feet anyways.")
        print(bag_message)
        user_input = input("Type 'totes!' to buy the bag or 'no' to pass")
        while user_input != "totes!" and user_input != "no":
            print("Type 'totes!' to buy it or 'no' to keep looking.")
            user_input = input()
        if user_input == "totes!":
            money = money - 30
        elif user_input == "no":
            print("You have plenty of bags at home anyways")

print(food_message)
user_input = input("Type 'si' for tacos or 'no' if you would rather eat at home")
while user_input != "si" and user_input != "no":
    print("Type 'si' for tacos or 'no' if you would rather eat at home")
    user_input = input()
if user_input == "si":
    money = money - 10
    if (money < 0):
        print("Oh no! You are $5 in debt!!! Next time, be mindful of the amount of money you are spending")
    elif (money > 0):
        print("Enjoy your Taco Bell! You have successfully completed your shopping trip with %d dollars still remaining" %(money))
elif user_input == "no":
    print("Hope you enjoyed you shopping trip! You have %d dollars left in your wallet" %(money))
