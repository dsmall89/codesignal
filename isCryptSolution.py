'''
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

* You have an array of strings crypt, the cryptarithm, 
  and an an array containing the mapping of letters and digits, solution. 

* The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], 
   which should be interpreted as the word1 + word2 = word3 cryptarithm.

* If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution,
  becomes a valid arithmetic equation containing no numbers with leading zeroes, 
  the answer is true. If it does not become a valid arithmetic solution, the answer is false.

 -> Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).
'''

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]


def isCryptSolution(crypt, solution):

    soldict = dict(solution)
    
    decrypt_result = []
    for word in crypt:
        dword = []
        for letter in word:
            
            #use letter to return value, then add value to array 
            dword.append(soldict[letter])
            print("dword : " + str(dword))
       
        #Check number for leading Zero,if encountered return false
        if len(dword) > 1 and dword[0] == '0':
            return False

        #concatnate & convert to number, then add to array
        decrypt_result.append(int(''.join(dword)))

        print("Decrypt Result: " + str(decrypt_result))
        
    return (decrypt_result[0] + decrypt_result[1] == decrypt_result[2])

print(isCryptSolution(crypt,solution))