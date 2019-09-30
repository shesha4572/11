def net_salary (salary):
    da = 0.2 * salary
    hra = 0.25 * salary
    net = salary + da + hra
    return net


def display (name, add, phn, salary, net):
    print("Employee's name            : ", name)
    print("Employee's address         : ", add)
    print("Employee's phone number    : ", phn)
    print("Basic salary               : ", salary)
    print("Net salary                 : ", net)


n = input("Enter employee's name : ")
a = input("Enter employee's address : ")
p = int(input("Enter employee's phone number : "))
s = float(input("Enter the basic salary : "))
net_s = net_salary(s)
display(n, a, p, s, net_s)


