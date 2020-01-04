str = input("Enter a string : ")
print("Entered string is :" , str)
str_capital = ""
lst = str.split()
for i in lst:
    str_capital += i.capitalize() + " "
print("String with first letter of all words capitalized :" , str_capital)