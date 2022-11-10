"""
#Question 1
for i in range(1, 11):
    print(i)
  
#Question 2
number = int(input("Give me a number: "))
sum = 0 
for i in range(1, number + 1):
    sum += i
print(sum)
 
#Question 3
for i in range(1500, 2701):
    if (i % 5 == 0):
        print(i)
    elif (i % 7 == 0):
        print(i)
        """
#Question 4
num = int(input("Enter Number: "))

for i in range(num+1):
    for k in range(1,i+1):
     print(k,end=" ")
    print()