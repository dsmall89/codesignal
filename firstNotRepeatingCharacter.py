def firstNotRepeatingCharactervoid(s):
    dup = set()
    for idx in range(len(s)):
        
        if s[idx] in dup:
            return s[idx]
            
        elif s[idx] not in dup:
            return "_"
        else:
          dup.add(s[idx])

    return -1


'''
O(n) solution
We loop through the string once. 
When we come across a new character, we store it in counts with a value of 1, and append it to acontainer . 

When we come across a character we've seen before, we increment its value in counts. 

Finally, we loop through aContainer until we find a character with a value of 1 in counts 
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


      
