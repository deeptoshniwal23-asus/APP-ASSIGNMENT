class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)
        print("Category :", self.category())
        print("---------------------------")


class Store:
    def __init__(self):
        self.mobile_list = []

    def add_mobile(self):
        brand = input("Enter Brand: ")
        model = input("Enter Model: ")
        price = int(input("Enter Price: "))   # Changed from str to int

        m = Mobile(brand, model, price)
        self.mobile_list.append(m)

        print("Mobile added successfully.\n")

    def display_mobiles(self):
        if len(self.mobile_list) == 0:
            print("No mobiles available.")
        else:
            print("\nMobile Details")
            print("====================")
            for mobile in self.mobile_list:
                mobile.display()


# Main Program
store = Store()

n = int(input("How many mobiles do you want to add? "))

for i in range(n):
    print("\nEnter details of Mobile", i + 1)
    store.add_mobile()

print("\nAll Mobiles in Store")
store.display_mobiles()



"""
How many mobiles do you want to add? 2

Enter details of Mobile 1
Enter Brand: Samsung 
Enter Model: S25 
Enter Price: 100000
Mobile added successfully.


Enter details of Mobile 2
Enter Brand: Redmi
Enter Model: Note 5 Pro
Enter Price: 20000
Mobile added successfully.


All Mobiles in Store

Mobile Details
====================
Brand : Samsung 
Model : S25
Price : 100000
Category : Premium
---------------------------
Brand : Redmi
Model : Note 5 Pro
Price : 20000
Category : Mid-range
---------------------------
"""
