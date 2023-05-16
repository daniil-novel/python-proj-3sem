#E711 comparison to None should be 'if cond is None:'

var = True
if var != True:
    print("var is not equal to True")
if var == None:
    print("var is equal to None")