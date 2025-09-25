print("Welcome to the Tip Calculator!")

# Get total bill amount from the user
try:
    bill = float(input("What was the total bill? $"))
except ValueError:
    print("Invalid input for bill. Please enter a number.")
    exit()

# Get desired tip percentage from the user
try:
    tip_percentage = int(input("How much tip would you like to give? (e.g., 10, 12, or 15) "))
    if not (0 <= tip_percentage <= 100):
        print("Tip percentage must be between 0 and 100.")
        exit()
except ValueError:
    print("Invalid input for tip percentage. Please enter a whole number.")
    exit()

# Get the number of people splitting the bill
try:
    num_people = int(input("How many people to split the bill? "))
    if num_people <= 0:
        print("Number of people must be greater than zero.")
        exit()
except ValueError:
    print("Invalid input for number of people. Please enter a whole number.")
    exit()

# Calculate the tip amount
tip_amount = bill * (tip_percentage / 100)

# Calculate the total bill including tip
total_bill_with_tip = bill + tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill_with_tip / num_people

# Format the final amount to two decimal places
final_amount_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount_per_person}")