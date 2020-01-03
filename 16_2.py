List1 = eval(input("Enter a list : "))
sum = 0
sum_odd = 0
sum_even = 0
num_even = 0
num_odd = 0
for i in range (0 , len(List1)):
    sum += List1[i]
    if List1[i] % 2 == 0 :
        sum_even += List1[i]
        num_even += 1
    else:
        sum_odd += List1[i]
        num_odd += 1

print("Sum of all elements in the list is", sum)
print("The sum of all even integers is " ,sum_even)
print("The sum of all odd integers is " ,sum_odd)
print("Number of elements in the list is" , len(List1))
print("Number of even numbers in the list is" , num_even)
print("Number of odd numbers in the list is" ,num_odd)

