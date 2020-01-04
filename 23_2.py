str = input("Enter the string to be searched : ")
sub_str = input("Enter the substring to be searched : ")
count = str.count(sub_str)
if count == 0:
    print("Given substring not found in string")
else:
    print("Given substring was found in string")
    print("Frequency :" , count)