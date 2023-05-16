import random
from collections import defaultdict
import inspect
import ast

from Module_3.Task_1.task_1 import mutate_code, make_mutants, mut_test


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        # TODO
        return node

    def mutate_code(src):
        tree = ast.parse(src)
        Mutator().visit(tree)
        return ast.unparse(tree)

    def make_mutants(func, size):
        mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
        mutants = [src]
        while len(mutants) < size + 1:
            while mutant in mutants:
                mutant = mutate_code(src)
            mutants.append(mutant)
        return mutants[1:]

    def mut_test(func, test, size=20):
        survived = []
        mutants = make_mutants(func, size)
        for mutant in mutants:
            try:
                exec(mutant, globals())
                test()
                survived.append(mutant)
            except:
                pass
        return survived

    #Новые функции
    def visit_BinOp(self, node):
        operators = [ast.Add, ast.Sub, ast.Mult, ast.Div]
        op = random.choice(operators)
        left, right = node.left, node.right
        if random.random() < 0.5:
            left = self.visit(left)
        else:
            right = self.visit(right)
        return ast.BinOp(left=left, op=op(), right=right)

    def visit_Compare(self, node):
        operators = [ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE]
        op = random.choice(operators)
        left, right = node.left, node.comparators[0]
        if random.random() < 0.5:
            left = self.visit(left)
        else:
            right = self.visit(right)
        return ast.Compare(left=left, ops=[op()], comparators=[right])

"""
visit_BinOp и visit_Compare. В каждом из них мы выбираем случайный оператор и два случайных операнда.
 Затем мы создаем новый узел BinOp или Compare с этими операндами и оператором. 
 Мы также добавили случайную вероятность выбора левого или правого операнда для замены.
"""
#Простая тестовая функция, создает случайный список и сравнивает его с
# отсортированным списком. Если они не совпадают, то вызывается исключение AssertionError.
def test_sort():
    lst = [random.randint(-100, 100) for _ in range(10)]
    sorted_lst = sorted(lst)
    assert lst == sorted_lst, f"Expected {sorted_lst}, but got {lst}"

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

survived = mut_test(bubble_sort, test_sort())
print(f"{len(survived)} mutants survived out of {size}")

