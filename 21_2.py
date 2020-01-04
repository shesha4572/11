lst = eval(input("Enter list to be sorted : "))
print("List before sorting:" , lst)
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("List after Bubble sorting:" , lst)