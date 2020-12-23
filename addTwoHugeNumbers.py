def testZip(a,b):
    a = "".join(map(str,a))
    b = "".join(map(str,b))
  

   
    return int(a) + int(b)
     

    # addList2 = map(lambda x: x*x, b)
    # return [sum(i) for i in zip(a, b)] 


a = [9876, 5432, 1999]
b = [1, 8001]

 
print("Reslut : " + str(testZip(a,b)))