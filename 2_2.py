def Simple(prin , rate , time):
    si = prin * rate * time / 100
    print("Simple interest is" ,si)

def Compound(prin , rate , time):
    ci = prin * (1 + rate/100) ** time
    print("Compound interest is" , ci)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time in years: "))
Simple(principal , rate , time)
Compound(principal , rate , time)