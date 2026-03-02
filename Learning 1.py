## First lesson, any task will be written and save here.
## Some lines of code are added or modified by me
item = input("What would you like to buy? ")
price = float(input("What price is it? "))
currency = input("What currency are you using? ")
quantity = float(input("How many would you like to buy? "))
total = price * quantity

print(f"You are buying {quantity} x {item}/s")
print(f"Your total is {total} {currency}")