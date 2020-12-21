# def isCryptSolution(crypt, solution):

def extractChar(crypt,solution):
    listtify_word= list(map(list,crypt))
    print(listtify_word)
    for i in crypt:

        for j in  i:

            for key,value in solution:
                if j == key:
                    print(value)

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