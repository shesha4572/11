def no_words(s):
    split_word = s.split(" ")
    return len(split_word)

def no_num(s):
    num = 0
    for i in range (0,len(s)):
        if  s[i].isdigit():
            num += 1
    return num

def no_alpha(s):
    alpha = 0
    for i in range (0,len(s)):
        if s[i].isalpha():
            alpha += 1
    return alpha

def no_special(s):
    special = 0
    for i in range (0, len(s)):
        if s[i].isalnum() == False:
            special += 1
    return special

string_check = input("Enter the string to be checked : ")
word = no_words(string_check)
num = no_num(string_check)
alpha = no_alpha(string_check)
spec = no_special(string_check)
print("The entered string is", string_check)
print("The number of words in the string is ", word)
print("The number of numeric characters in the entered string is ", num)
print("The number of alphabets in the entered string is ", alpha)
print("The number of special characters in the entered string is ", spec)