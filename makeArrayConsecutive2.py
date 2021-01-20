def makeArrayConsecutive2(statues):
    max_height = max(statues)
    min_height = min(statues)
    array_length  = len(statues)

    count_of_element = max_height - min_height + 1
    # '1 ' is added to make it inclusive
  
    return count_of_element-array_length