q = int(input("Enter a number : "))
w = int(input("Enter a number : "))
e = int(input("Enter a number : "))
r = int(input("Enter a number : "))
t = int(input("Enter a number : "))
y = int(input("Enter a number : "))
u = int(input("Enter a number : "))
i = int(input("Enter a number : "))
o = int(input("Enter a number : "))
p = int(input("Enter a number : "))
List1 = [q, w, e, r, t, y, u, i, o, p]
sum = 0
average = 0
for i in range (0,10) :
    sum += List1[i]
average = sum/10
print("The sum of all the elements in the list is ", sum)
print("The average of all the elements in the list is ", average)
