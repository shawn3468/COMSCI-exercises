
"""
#Question 1
d = {"apples": 15, "bananas": 35, "grapes": 12}
print(d)


a. 35
b. 4
c. True
d. Key does not exist
e. 0
f. ['apples', 'bananas', 'grapes', 'oranges']
g. False

#Question 3
def addFruit(inventory, fruit, quantity):
    #make this function work by adding code to it.
    inventory[fruit] = quantity
    return inventory

# Make these tests work...
new_inventory = {}
addFruit(new_inventory, "strawberries", 10)
assert "strawberries" in new_inventory, 'strawberries not added correctly'
assert new_inventory["strawberries"] == 10, 'strawberries value isn\'t correct'

addFruit(new_inventory, "strawberries", 25)
assert new_inventory["strawberries"] == 25,  'strawberries value isn\'t correct'
"""
def countChar(str):
    d = {}
    for i in range(26):
        d[i] = 0
    print(d)
    for i in str:
        print(i)
