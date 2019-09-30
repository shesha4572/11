def disp(s):
    print("Selected operation : Display the string")
    print(s)


def cpy_str(s):
    str1 = ""
    print("Selected operation : Copy the string")
    print("String before copying :" ,str1)
    str1 = s
    print("String after copying :" ,str1)


def concat_str():
    print("Selected operation : Concatenate the string")
    str1 = "Hello "
    str2 = "How are you?"
    print("String 1 :" ,str1)
    print("String 2 :" ,str2)
    print("After concatenation : " ,(str1 + str2))


a = input("Enter the string : ")
disp(a)
cpy_str(a)
concat_str()