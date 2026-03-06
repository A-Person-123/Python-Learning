## First mini project, any task will be written and save here.
## Some lines of code are added or modified by me
## This lesson is heavily modified by me. only the base functions are from tutorial rest is made by me
print("Welcome to basic calculator ")
Type_of_calc = int(input("If you would like to use basic functions (+, -, *, /) type 1, if you want to use powers and roots type 2: "))

if Type_of_calc == 1:
    operator = input("Type in your operator (+, -, *, /): ")
    num1 = int(input("Type in your first number: "))
    num2 = int(input("Type in your second number: "))
    if operator == "+":
        result = num1 + num2
        print(f"Your result is {round(result, 5)} rounded to 5 decimal places")
    elif operator == "-":
        result = num1 - num2
        print(f"Your result is {round(result, 5)} rounded to 5 decimal places")
    elif operator == "*":
        result = num1 * num2
        print(f"Your result is {round(result, 5)} rounded to 5 decimal places")
    elif operator == "/":
        result = num1 / num2
        print(f"Your result is {round(result, 5)} rounded to 5 decimal places")
    else:
        print(f"{operator} is not a valid operator!")
elif Type_of_calc == 2:
    operator = int(input("Type 1 for power, type 2 for root: "))
    num1 = int(input("Type the the number you would like to find the power/root of: "))
    num2 = int(input("Type the number you would like to power/root the first number by: "))
    if operator == 1:
        result = pow(num1, num2)
        print(f"The result is {round(result, 5)} rounded to 5 decimal places")
    elif operator == 2:
        result = num1 ** (1/num2)
        print(f"The result is {round(result, 5)} rounded to 5 decimal places")
    else:
        print("Invalid calculation")
else:
    print("That's not an existing type of calculator!")