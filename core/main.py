import sys
import numpy as np

from back import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT, FigureCanvasQTAgg


class Background(QThread):
    def __init__(self) -> None:
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self, note: Note) -> None:
        super().__init__()

        self.parser = CSVParser(note)
        self.observer = Observer(note)

        self.canvas = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.axes = self.canvas.figure.axes
        self.toolbar = NavigationToolbar2QT(self.canvas, self)


class StartWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

    def show_time(self) -> None:
        self.window = MainWindow(self.make_note())
        self.window.show()
        self.close()

    def make_note(self) -> Note:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())
