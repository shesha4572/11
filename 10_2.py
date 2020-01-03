def Reverse_String (s):
    s = s.lower()
    reversed = s[::-1]
    print("Reversed string is :  ", reversed )
    if reversed == s:
        return True
    else:
        return False
string_check = input("Enter the string to be checked :  ")
check = Reverse_String(string_check)
if check == True:
    print("The entered string is a palindrome")
else:
    print("The entered string is not a palindrome")
