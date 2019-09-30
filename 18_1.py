def change_case(char):
    char1 = char.swapcase()
    print("The entered character is" , char)
    if "A" <= char <= "Z":
        print("The entered character is in upper case")
        print("The character in lower case : " , char1)
    elif "a" <= char <= "z":
        print("The entered character is in lower case")
        print("The character in upper case : " , char1)
    else:
        print("The entered character is either a digit or a special character")


def Vote(age):
    if age >= 18:
        print("Congratulations !! You are eligible to vote ")
    else:
        print("Sorry :( You are not eligible to vote")



ch = input("Enter the character to be checked : ")
change_case(ch)
age = int(input("Enter your age : "))
Vote(age)





