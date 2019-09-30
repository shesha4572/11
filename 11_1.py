def sign_check(n):
    if n > 0 :
        print("The entered number is positive")
    elif n < 0:
        print("The entered number is negative")
    else:
        print("The entered number is neither positive nor negative")


def sumton(n):
    sum = (n+1)*n/2
    print("Sum to " +str(n)+ " natural numbers is " , sum)


a = int(input("Enter a number : "))
if a > 0 :
    sign_check(a)
    sumton(a)
else:
    sign_check(a)



