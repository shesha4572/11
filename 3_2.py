def Area_squ():
    side = float(input("Enter the length of side of square : "))
    area = side * side
    print("Area of square with side" , side , "is" ,area)

def Area_rect():
    len = float(input("Enter the length of rectangle : "))
    breadth = float(input("Enter the breadth of rectangle : "))
    area = len * breadth
    print("Area of rectangle is" , area)

def Area_cir():
    rad = float(input("Enter the length of radius of circle : "))
    area = 3.14 * rad * rad
    print("Area of circle with radius" , rad , "is" , area)

def Perimeter():
    len = float(input("Enter the length of rectangle : "))
    breadth = float(input("Enter the breadth of rectangle : "))
    peri = 2*(len + breadth)
    print("Perimeter of rectangle is" , peri)

print("1. Area of Square")
print("2. Area of Rectangle")
print("3. Area of Circle")
print("4. Perimeter of Rectangle")
num = int(input("Choose an option : "))
if num == 1:
    Area_squ()
elif num == 2:
    Area_rect()
elif num == 3:
    Area_cir()
elif num == 4:
    Perimeter()
else:
    print("Entered option is invalid")