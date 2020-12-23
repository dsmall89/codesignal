# -*- coding: utf-8 -*-
"""
We’re working on assembling a Game of Thrones family tree.

Example:

     Mad King         Rickard
     /     \          /    \
Daenerys  Rhaegar  Lyanna  Ned  Catelyn
              \    /         \  /
                Jon          Arya


Write a function that returns three collections:
-People who have no parents represented in our data
-People who only have 1 parent represented
-People who have 2 parents represented

Sample input:

familyGroups = [
    (‘Ned’, ‘Arya’), (‘Rhaegar’, ‘Jon’), (‘Lyanna’, ‘Jon’), (‘Catelyn’, ‘Arya’),
    (‘Mad King’, ‘Rhaegar’), (‘Rickard’, ‘Lyanna’), (‘Mad King’, ‘Daenerys’), (‘Rickard’, ‘Ned’)]

Sample output:
[‘Daenerys’, ‘Rhaegar’, ‘Lyanna’, ‘Ned’], -- One parent
[[‘Mad King’, ‘Rickard’, Catelyn], -- No parents
[‘Jon’, ‘Arya’]] -- Two parents


{'Arya' = 1,
 'Jon' = 2,
 'Lyanna' = 1}

"""

family_groups = [
    ("Ned", "Arya"), ("Rhaegar", "Jon"), ("Lyanna", "Jon"), ("Catelyn","Arya"),
    ("Mad King", "Rhaegar"),("Rickard", "Lyanna"), ("Mad King", "Daenerys"),
    ("Rickard", "Ned")]


def familyGroup(data):
    dict_Counter = {}
    #Seperate parents from Children by index
    parent_SetContainer = set()
    children_SetContainer= set()

    # Populate arrarys with parent groups
    people_with_one_parent= []
    people_with_two_parent= []

    for group in data:
        parent_SetContainer.add(group[0])
        children_SetContainer.add(group[1])
      
        if group[1] in dict_Counter.keys():
            dict_Counter[group[1]] += 1
        else:
            dict_Counter[group[1]] = 1
    # Results of dict_Counter shows the count of people's Parents
    # print('Show dict_Counter results :' + str(dict_Counter) + '\n')

    # Subtract parent - chilren 'sets' to get
    # people who have no parents represented in our data results
    diff_between_groups = parent_SetContainer - children_SetContainer
    # print(str(dict_Counter.items()) + '\n')

    for key, value in dict_Counter.items():
        if value ==1 :
            people_with_one_parent.append(key)
        else:
            people_with_two_parent.append(key)

    return [people_with_one_parent,people_with_two_parent,list(diff_between_groups)]
# print(familyGroup(family_groups))
