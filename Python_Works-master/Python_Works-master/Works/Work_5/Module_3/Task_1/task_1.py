import random
from collections import defaultdict
import inspect
import ast


def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int):
            node.value = random.randint(-100, 100)
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
    survived, scope = [], {}
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, scope)
            exec(inspect.getsource(test), scope)
            survived.append(mutant)
        except AssertionError:
            pass
    return survived


def test_bucketsort():
    arr = [3, 2, 1, 0]
    k = 4
    result = bucketsort(arr, k)
    expected = [0, 1, 2, 3]
    assert result == expected, f"Expected {expected}, but got {result}"


if __name__ == '__main__':
    survived = mut_test(bucketsort, test_bucketsort, size=100)
    if not survived:
        print("No survivors found, all mutants killed!")
    else:
        print(f"Survived mutants ({len(survived)}):")
        for mutant in survived:
            print(mutant)
