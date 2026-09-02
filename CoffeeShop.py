print("Welcome to the Python Coffee Shop!")
 
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")
 
price_coffee = 3.50
price_latte = 4.00
price_mocha = 5.00
 
print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_mocha))
 
choice = input("What would you like to order? (coffee/latte/Mocha or type No):').lower() ")

if choice == "coffee":
    cost = price_coffee
elif choice == "latte":
    cost = price_latte
elif choice == "Mocha":
    cost = price_mocha
else:
    print("Sorry, we do not have that.")
    cost = 0

    
if cost>0: 
    student = input("Are you student: (Yes/No)")
    quantity = int(input("How many cups would you like? "))
     
    total_cost = cost * quantity
     
    if quantity > 1:
        print("You get a discount of $1.00!")
        total_cost -= 1.00
    if student == "Yes":
        print("Great!  you will get 10% discount")
        total_cost = total_cost*0.90
     
    print("Your total is(str(round(total_cost))")
    print("Thank you, " + customer_name + "! Please come again.")
