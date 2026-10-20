# Electricity Bill Calculator
RATE = 12.90

#validate student name
name = input("Enter customer name: ")
if name.strip()=="":
    print("Invalid name. Please try again.")

#validate previous reading
previous = float(input("Enter previous meter reading: "))
if previous > 0:
    print("Previous meter reading", previous)
else:
    print("Invalid input. Please try again.")

#validate current reading
current = float(input("Enter current meter reading: "))
if current > previous:
    print("Current meter reading", current)
else:
    print("Invalid input. Please try again.")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
