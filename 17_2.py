def no_words(s):
    split_word = s.split(" ")
    print("The no of words in the string is" ,len(split_word))


def no_num(s):
    num = 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            num += 1
    print("The number of digits in the string is " ,num)


def no_alpha(s):
    alpha = 0
    upp = 0
    low = 0
    for i in range(0, len(s)):
        if s[i].isalpha():
            alpha += 1
            if "A" <= s[i] <= "Z":
                upp += 1
            else:
                low += 1

    print("The number of alphabets in the string is ", alpha)
    print("The number of uppercase alphabets in the string is ", upp)
    print("The number of lowercase alphabets in the string is ", low)


def no_special(s):
    special = 0
    for i in range(0, len(s)):
        if s[i].isalnum() == False:
            special += 1
    print("The number of special characters in the string is " ,special)


def len_str(s):
    len0 = len(s)
    print("The length of the string is " ,len0)


def disp(s):
    print("The string is : ", s)

str_user = input("Enter a string : ")
disp(str_user)
len_str(str_user)
no_words(str_user)
no_num(str_user)
no_alpha(str_user)
no_special(str_user)