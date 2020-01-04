lst = eval(input("Enter a list : "))
elem = eval(input("Enter the element to be searched : "))
count = 0
for i in range(0 , len(lst)):
    if lst[i] == elem:
        print("Element found at index" , i)
        count += 1

print("Frequency of element in list:" , count)
