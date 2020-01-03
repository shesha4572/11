def FtoC(temp) :
    temp_c = (temp-32)*5/9
    print(temp , "fahrenheit =", temp_c , "celcius" )


def CtoF(temp):
    temp_f = (temp*9/5) + 32
    print(temp, "celcius =" , temp_f, "fahrenheit")


temp = float(input("Enter the temperature : "))
unit = input("Enter the scale of temperature : F or C : ")
if unit == "F":
    FtoC(temp)
elif unit == "C":
    CtoF(temp)
else:
    print("Wrong Input")
