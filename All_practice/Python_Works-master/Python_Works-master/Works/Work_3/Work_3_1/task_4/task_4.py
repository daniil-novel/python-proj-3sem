from my_module import *

function1()   # работает
function2()   # вызовет NameError: name 'function2' is not defined
variable1     # работает
_variable2    # вызовет NameError: name '_variable2' is not defined