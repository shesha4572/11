def Armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

def Time(time):
    days = time // (24 * 60 * 60)
    time_hours = time - (days * 24 * 60 * 60)
    hours = time_hours // (60*60)
    time_min = time_hours - (hours * 60 * 60)
    min = time_min // 60
    sec = time_min - (min*60)
    print("Entered time in seconds :" , time)
    print("Number of days :" , days)
    print("Number of Hours :" , hours)
    print("Number of minutes :" , min)
    print("Number of seconds :" , sec)

number = int(input("Enter the number : "))
time_input = int(input("Enter the time in seconds : "))
Armstrong(number)
Time(time_input)