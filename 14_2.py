def Table(num):
    for i in range(1,11):
        print(num , "*" , i , "=" , num*i)

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
if a > b :
    if a > c :
        print(a , "is the greatest number")
        Table(a)
elif b > c:
    print(b , "is the greatest number")
    Table(b)
else:
    print(c , "is the greatest number")
    Table(c)