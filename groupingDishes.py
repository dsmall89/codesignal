def groupingDishes(dishes):

    dContainer = {}
    
    for l in dishes:
        dish = l[0]
        for i in l[1:]:
            if i not in dContainer:
                dContainer[i] = [dish]
            else:
                dContainer[i] += [dish]
                
    # print(d)
    
    out = []
    
    for i in sorted(dContainer):

        print("Sorted Dictionary -->" + str(dContainer))
        if len(dContainer[i]) > 1:
            out += [[i] + sorted(dContainer[i])]
            
    return out

dishes= [["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]

print(groupingDishes(dishes))