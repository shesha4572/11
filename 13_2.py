def calculate(m1, m2, m3, FullMarks):
    sum = m1 + m2 + m3
    average = sum / 3
    perc = (sum * 100) / (3 * FullMarks)
    print("The sum is ", sum)
    print("The average is ", average)
    print("The percentage is ", perc)
    if perc >= 80:
        print("The grade is A")
    elif perc >= 40:
        print("The grade is B")
    else:
        print("The grade is C")


mark1 = float(input("Enter the marks in subject 1 : "))
mark2 = float(input("Enter the marks in subject 2 : "))
mark3 = float(input("Enter the marks in subject 3 : "))
FullMarks = float(input("Enter the maximum possible marks in a subject : "))
calculate(mark1, mark2, mark3, FullMarks)
