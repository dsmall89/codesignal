def reserveString(s):
    output  = ""

    for currentletter in s:
        output = currentletter + " " + output

    return output
#(n^2) because of concatnation
print(reserveString(["a","b","c"]))