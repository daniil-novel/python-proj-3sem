'''
#E211 whitespace before '('
with open ('file.dat') as f:
    contents = f.read()

#E225 missing whitespace around operator
if age>15:
    print('Can drive')

#E231 missing whitespace after ','
my_tuple = 1,2,3

#E251 unexpected spaces around keyword / parameter equals
def func(key1 = 'val1',
         key2 = 'val2'):
    return key1, key2

#E302 expected 2 blank lines, found 1
def func1():
    pass
def func2():
    pass

#E701 multiple statements on one line (colon)
if x > 5: y = 10

#E702 multiple statements on one line (semicolon)
from gevent import monkey; monkey.patch_all()

#E711 comparison to None should be 'if cond is None:'
if var != True:
    print("var is not equal to True")
if var == None:
    print("var is equal to None")

#E712 comparison to True should be 'if cond is True:' or 'if cond:'
x = True
if x == True:
    print('True!')
'''
