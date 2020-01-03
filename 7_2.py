def Factorial(num):
    fact = 1
    for i in range(1, num):
        fact *= i
    print("Entered number is " , num)
    print("Factorial of", num , "is" , fact)


def LeapYear(year):
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return True
    elif year % 4 == 0:
        return True
    else:
        return False

num = int(input("Enter a number : "))
year = int(input("Enter year : "))
leap_year = LeapYear(year)
if leap_year == True:
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")
Factorial(num)