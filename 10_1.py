def fibonacci(n):
    first = 0
    second = 1
    print("Fibonacci series : " , end = " ")
    print(str(first) + "," + str(second), end = ",")
    for i in range(1 , n):
       next = first + second
       print(next, end = ",")
       first = second
       second = next
    print()



def prime(n):
    if n == 1:
        print("Neither composite nor prime")
    elif n == 2:
        print("Prime number")
    else:
        for i in range (2 , n):
            if n % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")


a = int(input("Enter a number : "))
fibonacci(a)
prime(a)
