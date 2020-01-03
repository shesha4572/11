List1 = eval(input("Enter a list : "))
sum_odd = 0
sum_even = 0
maximum = max(List1)
minimum = min(List1)
for i in range (0 , len(List1)):
    if List1[i] % 2 == 0 :
        sum_even += List1[i]
    else:
        sum_odd += List1[i]
print("The maximum value in the 10 entered integers is " ,maximum)
print("The minimum value in the 10 entered integers is " ,minimum)
print("The sum of all even integers is " ,sum_even)
print("The sum of all odd integers is " ,sum_odd)
