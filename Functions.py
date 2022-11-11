"""
#Question 1
def dayOfTheWeek(number):
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
    
numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    dayOfTheWeek(i)
   
#Question 2
    
def totalOfSum(number):
    sum = 0 
    for i in range(1, number + 1):
        sum += i
    print(sum)
     
number = int(input("Give me a number: "))
totalOfSum(number)

#Question 3
def menu():
    number = int(input("Press 1 for total of sum, press 2 for day of the week: "))
    if number == 1:
        x = int(input("Give me a number: "))
        totalOfSum(x)
    else:
        x = int(input("Give me a number between 0 and 6: "))
        dayOfTheWeek(x)
menu()
 """
#Question 4
def sumOfTwoInt(a, b):
    sum = a + b
    return sum
num = sumOfTwoInt(4, 8)
print(num)