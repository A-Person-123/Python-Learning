## Fourth lesson, any task will be written and save here.
## Some lines of code are added or modified by me

temp = float(input("What is the temperature? (Celsius) "))
is_raining = input("Is it raining? (Yes or No) ")

if temp > 35 or temp < 0 or is_raining == "Yes":
    print("The out door event is canceled")
else:
    print("The outdoor event is still scheduled")