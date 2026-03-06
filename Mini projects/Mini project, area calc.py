## First mini project, any task will be written and save here.
## Some lines of code are added or modified by me
## This lesson is heavily modified by me. only the base functions are from tutorial rest is made by me
choice = int(input("Enter whether you want to calculate the area of a square/rectangle or a triangle (type 1 for square/rectangle or type 2 for triangle): "))
if choice == 1:
    unit_of_measure = input("Enter the unit of measure: ") + "^2"
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = base * height
    print(f"The area of your square/rectangle is: {area} {unit_of_measure}")
elif choice == 2:
    unit_of_measure = input("Enter the unit of measure: ") + "^2"
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = base * height / 2
    print(f"The area of your triangle is {area} {unit_of_measure}")
elif choice <= 3 or choice > 1:
    print("Invalid choice")