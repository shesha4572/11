def gcd(a , b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a , b):
    return a * b / gcd(a , b)
c = int(input("Enter number 1 : "))
d = int(input("Enter number 2 : "))
print("Greatest Common Divisor :" , gcd(c , d))
print("Least Common Multiple :" ,lcm(c , d))
