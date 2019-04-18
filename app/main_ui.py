import sys
from PyQt5 import QtWidgets

from aplication.design import Ui_MainWindow
from core.data import Data


class AppView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # connections goes here
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        if self.radio_file.isChecked():
            file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file', '/home',
                                                              'Text file (*.txt);;All files (*)')[0]
            task = Data(file_name, from_file=True)
            self.brute_info_browser.append("Your's matrix:\n")
            self.bellman_info_browser.append("Your's matrix:\n")
            for row in task.matrix:
                tmp_string = '| '
                for item in row:
                    tmp_string += (str(item) + '   ')
                tmp_string += "  |"
                self.brute_info_browser.append(tmp_string)
                self.bellman_info_browser.append(tmp_string)
            task.solve()
            self.brute_info_browser.append('Solve results:\nAnswer: %s\nSolve time: % 1.6f seconds' %
                                           (task.result, task.resolve_time))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppView()
    window.setWindowTitle("Methods comparison")
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
