## Third lesson, any task will be written and save here.
## Some lines of code are added or modified by me
weight = float(input("What is your weight? "))
unit = input("Kilograms or pounds? (Kg or Lbs) ")

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 3)} {unit}")
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kg."
    print(f"Your weight is {round(weight, 3)} {unit}")
else:
    print(f"{unit} is not a valid unit")