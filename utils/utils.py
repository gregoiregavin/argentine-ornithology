def checkResults(nbOrders, nbFamilies, nbBirds) :
    
    check = True
    
    # Expected results
    EXP_ORDERS = 18
    EXP_FAMILIES = 35
    EXP_BIRDS = 204
    
    if nbOrders != EXP_ORDERS: 
        print('Something went wrong with Orders. Expected ' + str(EXP_ORDERS) + ', got ' + str(nbOrders) + '.')
        check = False 
    if nbFamilies != EXP_FAMILIES: 
        print('Something went wrong with Families. Expected ' + str(EXP_FAMILIES) + ', got ' + str(nbFamilies) + '.')
        check = False
    if nbFamilies != EXP_BIRDS : 
        print('Something went wrong with Birds. Expected ' + str(EXP_BIRDS) + ', got ' + str(nbBirds) + '.')
        check = False
    
    return check