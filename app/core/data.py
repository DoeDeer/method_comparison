"""
Module defines class, that contains single task data
"""
import numpy as np


class Data:
    """
    Class, that contains task matrix, task type and task result after solving
    """

    def __init__(self, matrix, task_type='max', from_file=False):
        assert isinstance(task_type, str), "'task_type' variable must be a string"
        assert task_type in ('min', 'max'), "'task_type' variable must take 'min' or 'max' value"
        self.task_type = task_type
        self.result = None
        if from_file:
            # uses matrix variable as path to file with matrix
            tmp = []
            file = open(matrix, 'r')
            for line in file:
                tmp.append(line.split(','))
            file.close()
            self.matrix = np.array(tmp)
            assert len(self.matrix.shape) == 2 and self.matrix.shape[0] == self.matrix.shape[1], "invalid matrix"
            for shape in self.matrix.shape[0]:
                self.matrix[shape][shape] = 0
        else:
            # uses matrix variable as object with numpy matrix
            assert isinstance(matrix, np.ndarray), "'matrix' variable must be a numpy.array instance"
            assert len(matrix.shape) == 2 and matrix.shape[0] == matrix.shape[1], "invalid matrix"
            self.matrix = matrix
            for shape in self.matrix.shape[0]:
                self.matrix[shape][shape] = 0
