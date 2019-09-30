def calculate_bill(units):
    cost = 0
    if units <= 100:
        cost = 0.4 * units
    elif units <= 300:
        cost = 40 + (0.5 * (units - 100))
    elif units <= 600:
        cost = 40 + 100 + (0.75 * (units - 300))
    elif units <= 1000:
        cost = 40 + 100 + 225 + (1 * (units - 600))
    else:
        cost = 40 + 100 + 225 + 400 + (1.5 * (units - 1000))
    return cost


def display(units, cost, name, date, month, year):
    print("Date of the bill           : " + str(date) + '/' + str(month) + '/' + str(year))
    print("Name of the customer       : ", name)
    print("Total no of units consumed : " , units)
    print("Total cost                 : " , cost)


def main ():
    name = input("Enter the name of the customer : ")
    date = int(input("Enter the  date : "))
    month = int(input("Enter the month : "))
    year = int(input("Enter the year : "))
    units = int(input("Enter the number of units consumed : "))
    cost = calculate_bill(units)
    display(units , cost, name, date, month, year)


check = input("Do u want to run this program ? Y or N : ")
if check == 'Y':
    main()
