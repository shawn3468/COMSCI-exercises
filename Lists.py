#Question 1
spam = ['a','b','c','d']
print(spam[2])
spam[2] = "Hello"
print(spam[2])

#Question 2
spam[(3 * 2) // 11]
print(spam[(3 * 2) // 11])

#Question 3
print(spam[-1])

#Question 4
#Question 4 has a index out of range

#Question 5
spam[:2]
print(spam[:2])
#Question 6
bacon = [3.14, 'cat', 11, 'cat', True]
bacon.index('cat')
print(bacon.index('cat'))                    
print(bacon[1])
#Question 7
bacon.append(99)
print (bacon)
#bacon.append make the list value bacon have another value added to the end of it

#Question 8
bacon.remove('cat')
print(bacon)
#It only removes the first one that goes in order, starting off at the 0 index

#Question 10
#The difference between append and insert is that for insert you can insert the value where you choose to. Append can only insert the value at the end.

#Question 11
#.remove, clear()

#Question 12
spam = ['apples', 'bananas', 'tofu', 'cats']
print(spam[0] +", "+spam[1] +", "+spam[2] +", and "+spam[3])
