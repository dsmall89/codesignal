'''
Given a string s consisting of small English letters, 
find and return the first instance of a non-repeating character in it.
 If there is no such character, return '_'.
'''

'''
O(n) solution
1. We loop through the string once. 

2. When we come across a new character, we store it in dcontainer with a value of 1, and append it to acontainer . 

3. When we come across a character we've seen before, we increment its value in dcontainer. 

4. Finally, we loop through aContainer until we find a character with a value of 1 in dcontainer 
and return it.
'''



def firstNotRepeatingCharacter(input):
    aContainer = []
    dcontainer = {}
    
    for idx in input:
        
        if idx in dcontainer:
            dcontainer[idx] += 1
        else:
            dcontainer[idx] = 1 
            aContainer.append(idx)
        
    for val in aContainer:
        
        if dcontainer[val] == 1:
            
            return val
            
    return "_"

s = "abacabad"
#print(firstNotRepeatingCharacter(s))


      
