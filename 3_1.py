def series1() :
    for i in range (1 , 86 , 2):
        print(i , end = " ,")
    print()


def series2():
    sum = 0
    for a in range(1, 21 , 3):
        sum += a
    print("The sum of the series is 1 + 4 + 7+ ...20 is " ,sum)


series1()
series2()