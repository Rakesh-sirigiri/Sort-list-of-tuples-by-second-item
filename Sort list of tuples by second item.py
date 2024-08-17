def Sort_Tuple(tup):
    return(sorted(tup, key = lambda x: x[1]))
tup = [('rishav', 10), ('akash',5), ('ram',20), ('gaurav',15)]
print(Sort_Tuple(tup))
