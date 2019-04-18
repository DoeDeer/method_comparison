import sys
from PyQt5 import QtWidgets

from aplication.design import Ui_MainWindow
from core.data import Data


class AppView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.task = None
        # connections goes here
        self.pushButton.clicked.connect(self.calc)
        self.input_button.clicked.connect(self.set_matrix)
        self.radio_file.toggled.connect(self.button_title_set_file)
        self.radio_keyboard.toggled.connect(self.button_title_set_kb)

    def calc(self):
        if not self.task:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enter matrix first!")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.brute_info_browser.append("Your's matrix:\n")
            self.bellman_info_browser.append("Your's matrix:\n")
            for row in self.task.matrix:
                tmp_string = '| '
                for item in row:
                    tmp_string += (str(item) + '   ')
                tmp_string += "  |"
                self.brute_info_browser.append(tmp_string)
                self.bellman_info_browser.append(tmp_string)
            first_city = self.first_city_spin_box.value()
            first_city = first_city if first_city != 1 else None
            self.task.solve(first_city=first_city)
            self.brute_info_browser.append('Solve results:\nAnswer: %s\nSolve time: % 1.6f seconds' %
                                            (self.task.result, self.task.resolve_time))

            self.task.solve(method='dynamic', first_city=first_city)
            self.bellman_info_browser.append('Solve results:\nAnswer: %s\nSolve time: % 1.6f seconds' %
                                                (self.task.result, self.task.resolve_time))

    def set_matrix(self):
        if self.radio_file.isChecked():
            file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file', '/home',
                                                              'Text file (*.txt);;All files (*)')[0]
            if file_name:
                task_type = 'min'
                if self.max_type_radio.isChecked():
                    task_type = 'max'
                self.task = Data(file_name, task_type=task_type, from_file=True)
                self.first_city_spin_box.setMaximum(len(self.task.matrix))
        if self.radio_keyboard.isChecked():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Enter matrix first!")
            msg.setWindowTitle("Matrix error")
            msg.exec_()

    def button_title_set_file(self):
        self.input_button.setText('Choose file')

    def button_title_set_kb(self):
        self.input_button.setText('Enter matrix')




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppView()
    window.setWindowTitle("Methods comparison")
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
