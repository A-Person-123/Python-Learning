## Fifth lesson, any task will be written and save here.
## Some lines of code are added or modified by me

temp = float(input("What is the temperature? (Celsius) "))
is_sunny = input("Is it sunny? (Yes or No) ")

if temp >= 15 and is_sunny == "Yes":
    print("It is HOT and SUNNY")
elif temp <= 14 and is_sunny == "Yes":
    print("It is COLD and SUNNY ")
elif temp >= 15 and is_sunny == "No":
    print("It is HOT and CLOUDY ")
elif temp <= 14 and is_sunny == "No":
    print("It is COLD and CLOUDY ")
else:
    print("You did not put 'Yes' or 'No' for 'Is it sunny'")