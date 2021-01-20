'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
'''



def adjacentElementsProduct(inputArray):
    finalArray = []
    
    for idx in range(len(inputArray) - 1):

        finalArray.append(inputArray[idx] * inputArray[idx+1])
        
        result = max(finalArray)
        
    return result

