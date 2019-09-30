List = [None,None,None,None,None,None,None]
for i in range (1, len(List)):
    List[i] = input("Enter item in the list : ")
char = input("Enter the item to be found : ")
num_instance = 0
pos_instance = ""
found1 = 0
for a in range (0 , len(List)):
    if List[a] == char:
        num_instance += 1
        pos_instance += str(a) + ","
        found1 = 1

if found1 == 0:
    print("The entered character is not in the list")
else :
    print("The entered character is present at position ", pos_instance)
    print("The entered character is repeated ", num_instance, " times")

