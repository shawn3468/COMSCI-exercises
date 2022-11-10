"""
#Question 1
a > b - b > a
a >= b - b >= a
a >= 18  and  day == 3 - 3 != day and 18 >= a
a >= 18  and  day != 3 - 3 == day and 18 >= 
#Question 2 
3 == 3 True
3 != 3 False
3 >= 4 False
not (3 < 4) True

#Question 3
number = int(input("Choose a number: "))
if number == 0:
    print("Sunday")
elif number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
    """
#Question 4
numDay = int(input("What number day was it: "))
length = int(input("Length of you're stay: "))
endDay = (length + numDay) % 7
day = ""
if endDay == 0:
    day = ("Sunday")
elif endDay == 1:
    day = ("Monday")
elif endDay == 2:
    day = ("Tuesday")
elif endDay == 3:
    day = ("Wednesday")
elif endDay == 4:
    day = ("Thursday")
elif endDay == 5:
    day = ("Friday")
elif endDay == 6:
    day = ("Saturday")
print("Vacation ends on "+ day)