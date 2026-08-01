class Pizza:
    def order(self):
        print("Pizza order has been placed")


class Burger:
    def order(self):
        print("Burger order has been placed")


class Sandwich:
    def order(self):
        print("Sandwich order has been placed")


class FoodOrder:
    def __init__(self, item):
        self.item = item

    def place_order(self):
        self.item.order()


print("Select Food Item")
print("1. Pizza")
print("2. Burger")
print("3. Sandwich")

choice = int(input("Enter your choice: "))

if choice == 1:
    food = FoodOrder(Pizza())
elif choice == 2:
    food = FoodOrder(Burger())
elif choice == 3:
    food = FoodOrder(Sandwich())
else:
    print("Invalid Choice")
    exit()

food.place_order()


"""
Select Food Item
1. Pizza
2. Burger
3. Sandwich
Enter your choice: 2
Burger order has been placed

"""
