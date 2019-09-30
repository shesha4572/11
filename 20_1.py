def one():
    num = 5
    for i in range(5, 0, -1):
        for j in range(i, 6):
            print(j, end="")
        print()


def two():
    string = ""
    for i in range(1, 6):
        string = str(i)
        print(string * i)


def three():
    num = 0
    for i in range(1, 6):
        num = (num * 10) + i
        print(num)


one()
two()
three()
