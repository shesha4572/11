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
even_sum = 0
odd_sum = 0
for a in range(0,10):
    if List1[a] % 2 == 0:
        even_sum += List1[a]
    else:
        odd_sum += List1[a]

print("The sum af all even numbers in the list is ", even_sum)
print("The sum  of all odd numbers in the list is ", odd_sum)
