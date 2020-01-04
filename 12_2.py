sales = float(input("Enter the sales of the salesman: "))
bonus = 0
if sales >= 10000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.07
print("Sales           :" ,sales)
print("Bonus           :" ,bonus)
