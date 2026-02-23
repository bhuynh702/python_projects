"""

File: list_merge.py
Author: Brittany Huynh
E-mail: bhuynh4@umbc.edu
Date: 09/2023
Description: This file adds elements from 2 lists together.

"""

# Ask for number of elements in first list 
num_ele = int(input('How many elements do you want in each list? '))

# Create empty list to store inputs from first set of questions
list1 = []

# first 'for i' loop for (num_ele) set of questions 
for i in range(0,num_ele):
    ele1 = input('What do you want to put in the first list? ') 
    for i in ele1[0]: 
        list1.append(ele1) # nested loop to add (ele1) into first list 
        
# do the same for the second set of questions 
list2 = []
for i in range(0,num_ele):
    ele2 = input('What do you want to put in the second list? ')
    for i in ele2[0]:
        list2.append(ele2)

# the 3rd list will combine the 1st and 2nd list
list3 = []
for i in range(0,num_ele):
    list3.append(list1[i])
    list3.append(list2[i])

print('The first list is:',list1)
print('The second list is:',list2)
print('The merged list is:',list3)
