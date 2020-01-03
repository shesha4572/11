def series(num):
    sum0 = 0
    for i in range(0, (n + 1)):
        sum0 += i*(i + 1)/2
    print("The sum of the series 1 + (1+2) + (1+2+....+"+str(n)+ ")"
                                                                 " is ", sum0)


n = int(input("Enter the number : "))
series(n)