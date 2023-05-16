GLOBAL_VAR = 0

def set_global_var(new_value):
    global GLOBAL_VAR
    GLOBAL_VAR = new_value

def get_global_var():
    return GLOBAL_VAR