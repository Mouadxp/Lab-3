# Author: Mouad EL Baraka
# Date: 2025-05-24
# This program simulates a simple shopping cart.
# Users can add items, specify quantities, and see the total cost.
# The program uses exception handling to manage invalid inputs.

print("Welcome to the Shopping Cart Program!")
user_input = ""
while user_input != "n":
    try:
        numOfItems = int(input("Please enter the Number of items: "))
        count = 0
        total_cost = 0

        while count < numOfItems :
            try:
                name =input(f"What is the name of item number {count+1}: ")
                price = float(input("what is the price of the item: $"))
                quantity = float(input("How many did you get: "))
                total = price * quantity
                total_cost += total
            except:
                print("Could not calculate the total")
                count = numOfItems
            count+=1
            
        print(f"The total cost of your Purchase is ${total_cost:.2f}")

        if total_cost > 100:
            discount = total_cost * 0.1
            total_cost -= discount
            print(f"\nYou saved ${discount:.2f} with a 10% discount!")
            print(f"Discounted Total: ${total_cost:.2f}")
            
    except:
        print("Invalid number f items input")

    user_input = input("\nWould you like to shop again? (yes/no): ").lower()
print("Thank you for shopping with us!")
