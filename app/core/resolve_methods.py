"""
Methods for solving TSP
"""
from itertools import permutations


def brute_force(matrix, task_type='max'):
    res_func = {'max': max, 'min': min}[task_type]
    res = {'max': -1, 'min': 99999999999}[task_type]
    for permutation in permutations(range(len(matrix[0]))):
        tmp_res = matrix[permutation[-1]][permutation[0]]
        for num, el in enumerate(permutation[:-1]):
            tmp_res += matrix[el][permutation[num + 1]]
        res = res_func(res, tmp_res)
    return res
