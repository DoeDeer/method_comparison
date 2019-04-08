"""
Methods for solving TSP
"""
from itertools import permutations


def brute_force(matrix, task_type='max', first_city=None):
    res_func = {'max': max, 'min': min}[task_type]
    res = {'max': -1, 'min': 99999999999}[task_type]
    if first_city:
        assert isinstance(first_city, int), "'first_city' variable must be an integer"
        first_city -= 1
        perms = (permutation for permutation in permutations(range(len(matrix[0]))) if permutation[0] == first_city)
    else:
        perms = permutations(range(len(matrix[0])))
    for permutation in perms:
        tmp_res = matrix[permutation[-1]][permutation[0]]
        for num, el in enumerate(permutation[:-1]):
            tmp_res += matrix[el][permutation[num + 1]]
        res = res_func(res, tmp_res)
    return res
