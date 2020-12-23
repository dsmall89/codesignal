'''
[4,12,9,5,6]
[4,9,12,6]
'''

def find_missing(fullset, partial_set):
    missing_items = set(fullset) - set(partial_set)
    assert(len(missing_items)==1)
    return list(missing_items)[0]

fullset = [4,12,9,5,6]
partial_set = [4,9,12,6]
#print(find_missing(fullset, partial_set))


def find_missing_xor(fullset, partial_set):
    xor_sum = 0
    for num in fullset:
        import pdb; pdb.set_trace()
        xor_sum ^=num
        print(xor_sum)
    for num in partial_set:
        xor_sum ^=num
    return xor_sum

fullset = [4,12,9,5,6]
partial_set = [4,9,12,6]
print(find_missing_xor(fullset, partial_set))