List1 = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i']      #The list to be searched
def search(char , list_search):                                    #char is the char which is to be searched in the list
    len0 = len(list_search)
    for i in range (0 , len0):
        if list_search[i] == char:
            print("The object " +char+ " is present in the list at position " ,i)
            break
    else:
        print("The object " +char+ " is not present in the list")


q = input("Enter the character to search : ")                      #Getting the element to be searched from the user
search(q , List1)                                                  #Calling method search() to search the given element in the list

