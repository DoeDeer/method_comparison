"""
Module defines class, that contains single task data
"""
import numpy as np


class Data:
    """
    Class, that contains task matrix, task type and task result after solving
    """

    def __init__(self, matrix, task_type='max', from_file=False):
        assert isinstance(task_type, str), "'task_type' must be a string"
        assert task_type in ('min', 'max'), "'task_type' must take 'min' or 'max' value"
        self.t_type = task_type
        self.result = None
        if from_file:
            # uses matrix variable as path to file with matrix
            pass
        else:
            # uses matrix variable as object with numpy matrix
            pass
