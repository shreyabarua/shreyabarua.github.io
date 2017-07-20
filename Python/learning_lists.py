# LEVEL 1
names = ["Jacqueline", "Shreya", "Josephine", "Bella", "Melinda", "Maria", "Rebekah", "Lina", "Lea", "Abigail", "Faith"]
num_names = int(input("How many names do you want to print?"))
for x in range(num_names):
    print(names[x])
pick_name = int(input("Pick a number from 0 to 10"))
print(names[pick_name])
# LEVEL 2
from random import randint
sides = ["soup", "mashed potatoes", "mac&cheese", "fries", "mixed veggies"]
main = ["pasta", "burger", "baked salmon", "chicken&rice", "cobb salad"]
dessert = ["ice cream", "cake", "creme brulee", "fruit", "pie"]
num_meals = int(input("How many meals would you like?"))
for s in range(num_meals):
    print (sides[randint(0, 4)])
    print (main[randint(0, 4)])
    print (dessert[randint(0, 4)])
    print("")
# LEVEL 3
three_syll = [""]
