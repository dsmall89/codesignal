
from pprint import pprint 

def addListasValue(my_list):
    if len(my_list) == 0:
        return -1

    my_dict = {}

    for key in my_list:
        indices = []

        for index,value in enumerate(my_list):

            if value == key:
                indices.append(index)

        my_dict[key] = indices

    return my_dict

a = [2, 1, 3, 5, 3, 2]

pprint(addListasValue(a))

'''
Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which the second 
occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.
'''

def firstDuplicate(a):
    dup = set()
    for idx in range(len(a)):

        if a[idx] in dup:
            return a[idx]
        else:
            dup.add(a[idx])
            print(dup)

    return -1

val = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(val))