'''
2.1.
[0xfor _ in 'abc']
краткий способ создания списков с использованием одной строки кода.
Понимание списка в этом коде создает список длиной 3,
где каждый элемент является значением 0x0( 0в шестнадцатеричном формате),
поскольку for _ in 'abc'выполняется три итерации,
с _представлением одноразовой переменной, поскольку она не используется внутри цикла.
Таким образом, результирующий список будет [0x0, 0x0, 0x0].
'''


# 2.2
def named_args_only(*args, **kwargs):
    if kwargs:
        return kwargs
    else:
        raise TypeError('Positional arguments are not allowed')


named_args_only(foo=1, bar=2)
# named_args_only(1, 2)


# 2.3
'''
1)В приведенном вами примере aи bприсваивается целочисленное значение 1,
а cи dприсваивается целочисленное значение 300000. При сравнении a и bс isоператором результат равен True,
что означает, что они являются одним и тем же объектом в памяти. Это связано с тем,
что Python кэширует небольшие целочисленные объекты в диапазоне от -5 до 256,
поэтому любые переменные, которым присвоены эти значения, будут ссылаться на один и тот же объект в памяти.

Однако при сравнении cи dс isоператором результат будет False, что означает, что они не являются одним и тем же объектом в памяти.
 Это связано с тем, что Python не кэширует большие целочисленные объекты, как маленькие.    
Когда вы присваиваете c и d значение 300000,
 им присваиваются два разных целочисленных объекта в памяти.

Важно отметить, что в то время как is оператор сравнивает идентичность объекта, == оператор сравнивает равенство объектов.

2) Это возможно, потому что оператор is проверяет, имеют ли два объекта одинаковую идентичность
(т. е. являются ли они одним и тем же объектом в памяти), а оператор == проверяет, имеют ли два объекта одинаковое значение.
В этом случае a и b являются одним и тем же объектом в памяти, поэтому сравнение is возвращает True.
Однако a и c имеют одно и то же значение, но разные идентификаторы, поэтому сравнение == возвращает True, а сравнение is возвращает False.
'''

# 2.4
i = 0
['much', 'code', 'wow'][i][0]  # 19
